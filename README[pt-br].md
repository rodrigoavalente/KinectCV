KinectCV
========

Softwares de visão computacional com Kinect.

Dependências
------------

- [OpenCV](https://github.com/Itseez/opencv)
- [Openkinect](https://github.com/OpenKinect/libfreenect)

Detecção de Faces
-----------------

É possível realizar a detecção de faces através de uma comparação em cascata. A biblioteca OpenCV oferece algoritmos já prontos para isso, basta carregar um arquivo que contém os dados para faces e indicar o local onde as faces devem ser procuradas.

```python    
    # Carrega a base de dados para a comparação
    face_cascade =  face_cascade = cv.CascadeClassifier(
            "haarcascades/haarcascade_frontalface_default.xml")
    # Faz a busca pelos rostos retornando um objeto
    # com todos os rostos encontrados
    faces = face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.2,
                minNeighbors=3,
                minSize=(50, 50),
                flags=cv.cv.CV_HAAR_SCALE_IMAGE)
    # Navega pelo objeto desenhando um retângulo na
    # imagem original no local onde foi encontrado as faces.
    for (point_x, point_y, width, height) in faces:
        self.draw_rectangle((point_x, point_y),
                            (point_x + width, point_y + height))
```
