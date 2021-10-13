import pytesseract
import cv2
import os
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = R'C:/Program Files/Tesseract-OCR/Tesseract'


#이미지를 불러와 gray 스케일로 변환해 준다.

image = cv2.imread('sample.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((52,2), np.uint8)
kernel2 = np.ones((6,15), np.uint8)
