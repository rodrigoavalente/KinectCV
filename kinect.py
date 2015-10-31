import freenect
import cv2 as cv
import numpy as np
import threading


class KinectThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)


class Kinect():
    def __init__(self):
        self.rgb = []
        self.depth = []
        self.video = []

    def detect_frontal_face(self):
        if len(self.rgb):
            face_cascade = cv.CascadeClassifier(
                "haarcascades/haarcascade_frontalface_default.xml")
            gray_frame = cv.cvtColor(self.rgb, cv.COLOR_BGR2GRAY)
            gray_frame = cv.equalizeHist(gray_frame)
            faces = face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.2,
                minNeighbors=3,
                minSize=(50, 50),
                flags=cv.cv.CV_HAAR_SCALE_IMAGE)

            if len(faces):
                for (point_x, point_y, width, height) in faces:
                    self.draw_rectangle((point_x, point_y),
                                        (point_x + width, point_y + height))

    def detect_profile_face(self):
        if len(self.rgb):
            face_cascade = cv.CascadeClassifier(
                "haarcascades/haarcascade_profileface.xml")
            gray_frame = cv.cvtColor(self.rgb, cv.COLOR_BGR2GRAY)
            gray_frame = cv.equalizeHist(gray_frame)
            faces = face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.2,
                minNeighbors=3,
                minSize=(50, 50),
                flags=cv.cv.CV_HAAR_SCALE_IMAGE)

            if len(faces):
                for (point_x, point_y, width, height) in faces:
                    self.draw_rectangle((point_x, point_y),
                                        (point_x + width, point_y + height))

    def draw_rectangle(self, first_point, second_point, color=(0, 102, 204)):
        cv.rectangle(img=self.rgb,
                     pt1=first_point,
                     pt2=second_point,
                     color=color,
                     thickness=2,
                     lineType=8)

    def show(self, detect_face):
        while True:
            (self.rgb, _) = freenect.sync_get_video()
            (self.depth, _) = freenect.sync_get_depth()
            self.depth = np.dstack(
                        (self.depth, self.depth, self.depth)).astype(np.uint8)
            if detect_face:
                frontal_face = KinectThread(self.detect_frontal_face)
                profile_face = KinectThread(self.detect_profile_face)
                frontal_face.start()
                profile_face.start()
                frontal_face.join()
                profile_face.join()

            self.video = np.hstack((self.depth, self.rgb))
            cv.imshow("Kinect Video", np.array(self.video[::1, ::1, ::-1]))
            if cv.waitKey(5) == 27:
                cv.destroyAllWindows()
                break


kinect = Kinect()
kinect.show(True)
