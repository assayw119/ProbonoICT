import speech_recognition as sr
from gtts import gTTS
import os 
import time
import playsound 

def speak(text):
	tts = gTTS(text = text, lang = 'ko')
	filename = '다시.mp3'
	tts.save(filename)
	playsound.playsound(filename)



speak('가격표를 다시 인식하여주세요') 


 