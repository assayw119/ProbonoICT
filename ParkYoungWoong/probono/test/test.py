import pytesseract
import cv2
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = R'C:/Program Files/Tesseract-OCR/Tesseract'


#이미지를 불러와 gray 스케일로 변환해 준다.

image = cv2.imread('sample.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#pytesseract에서는 numpy array를 읽지 못하고 file을 읽기 때문에 os로 파일을 불러들여야 한다.
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)

#pytesseract의 image to string을 써준다. 
#숫자니까 lang = 'None'으로

text = pytesseract.image_to_string(Image.open(filename), lang='kor+eng')
os.remove(filename)

#결과를 보자.

print(text)
cv2.imshow('img',image)
cv2.waitKey(0)