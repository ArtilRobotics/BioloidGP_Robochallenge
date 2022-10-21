from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

time.sleep(0.1)

video = cv2.VideoCapture('Video.mp4')
i = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
  if i == 20:
    bgGray = gray
  if i > 20:
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    # Para OpenCV 3
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Para OpenCV 4
    #cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, cnts, -1, (0,0,255),2)        
    
    for c in cnts:
      area = cv2.contourArea(c)
      if area > 9000:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
  cv2.imshow('Frame',frame)
  i = i+1
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()