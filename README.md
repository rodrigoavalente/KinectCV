Avaible Languages:
=================
- [pt-br](README[pt-br].md)


KinectCV
--------
Computer Vision softwares with Kinect.

Dependencies
------------

- [OpenCV](https://github.com/Itseez/opencv)
- [Openkinect](https://github.com/OpenKinect/libfreenect)

Face Detection
-----------------

It's possible to find faces in captured video or picture through the cascade compartion. The OpenCV lib offers algoritms for taht, all you need to do is load a file that have the data for the face comparation and point the source for the faces to be found.

```python
    # Load the cascade file
    face_cascade =  face_cascade = cv.CascadeClassifier(
            "haarcascades/haarcascade_frontalface_default.xml")
    # Do the search, returning an object
    # with all the faces found.
    faces = face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.2,
                minNeighbors=3,
                minSize=(50, 50),
                flags=cv.cv.CV_HAAR_SCALE_IMAGE)
    # Draw an rectangle in the video source for each of the
    # faces found.
    for (point_x, point_y, width, height) in faces:
        self.draw_rectangle((point_x, point_y),
                            (point_x + width, point_y + height))
```
