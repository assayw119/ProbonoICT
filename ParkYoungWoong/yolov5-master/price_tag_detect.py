
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2

facenet = cv2.dnn.readNet('best.pt')
model = load_model('models/yolov5s.yaml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret == False:
        break

    h, w, c = img.shape

    blob = cv2.dnn.blobFromImage(img, size=(300, 300), mean=(104., 177., 123.))
    facenet.setInput(blob)
    dets = facenet.forward()

    for i in range(dets.shape[2]):
        confidence = dets[0, 0, i, 2]

        if confidence < 0.5:
            continue

        x1 = int(dets[0, 0, i, 3] * w)
        y1 = int(dets[0, 0, i, 4] * h)
        x2 = int(dets[0, 0, i, 5] * w)
        y2 = int(dets[0, 0, i, 6] * h)

        face = img[y1:y2, x1:x2]

        face_input = cv2.resize(face, dsize=(224, 224))
        face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB)
        face_input = preprocess_input(face_input)
        face_input = np.expand_dims(face_input, axis=0)

        mask, nomask = model.predict(face_input).squeeze()

        if mask > nomask:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color)

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break
