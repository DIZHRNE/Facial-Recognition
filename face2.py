"""
If person is known, opens GUI
"""
import face_recognition
import cv2
import os
import glob
import numpy as np
import webbrowser

faces_dir = 'known_faces/'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
encoding_for_image = []

cam = cv2.VideoCapture(0)
retval, frame = cam.read()
if retval != True:
    raise ValueError("Can't read frame")

cv2.imwrite('person.png', frame)

for img in os.listdir(faces_dir):
        image = faces_dir + img
        image = face_recognition.load_image_file(image)
        image_encoding = face_recognition.face_encodings(image) 
        encoding_for_image.append(image_encoding[0])

unknown_image = face_recognition.load_image_file("person.png")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([encoding_for_image], unknown_encoding) 

for elem in results:
    if [True]:
        print("Person is known, will unlock")
        exec(open("gui.py").read())