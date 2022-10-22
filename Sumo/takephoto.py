from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
camera.start_preview()
sleep(5)
camera.capture('dojiotest2.jpg')
camera.stop_preview()