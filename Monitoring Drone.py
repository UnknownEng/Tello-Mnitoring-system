from djitellopy import tello
import time
from time import sleep
import cv2
import kp

me = tello.Tello()

global img  #making img variable global

me.connect()
print("Connected.....")

print("Checking Battery")
print("Battery is", me.get_battery())

print("Initiallizing KeyBoard")
kp.init()

print("Starting CAmera")
me.streamon()
print("Camera Initialized")

print("Taking Off Drone")
me.takeoff()

#KeyBoard

def move():
    if kp.getKey("a"):
        me.send_rc_control(30,0,0,0)
        print("move Left")
        sleep(3)
    elif kp.getKey("d"):
        me.send_rc_control(-30,0,0,0)
        print("move right")
        sleep(3)
    elif kp.getKey("w"):
        me.send_rc_control(0,30,0,0)
        print("move  forward")
        sleep(3)
    elif kp.getKey("s"):
        me.send_rc_control(0,0,0,0)
        print("Hovering")
        sleep(3)
    elif kp.getKey("x"):
        me.send_rc_control(0,-30,0,0)
        print("move backward")
        sleep(3)
    elif kp.getKey("UP"):
        me.send_rc_control(0,0,30,0)
        print("move upward")
        sleep(3)
    elif kp.getKey("DOWN"):
        me.send_rc_control(0,0,-30,0)
        print("move downward")
        sleep(3)
    elif kp.getKey("z"):
        me.send_rc_control(0,0,0,30)
        print("Rotate clockwise")
        sleep(3)
    elif kp.getKey("c"):
        me.send_rc_control(0,0,0,-30)
        print("move anticlockwose")
        sleep(3)
    elif kp.getKey("v"):
        me.land()
        print("landed")
        
    elif kp.getKey("b"):
        me.takeoff()
        print("TAking OFF")
        
    elif kp.getKey("p"):
        print("taking image")
        cv2.imwrite(f'{time.time()}.jpg' , img)
        sleep(0.3)
        print("image is")

while True:
    move()
    img = me.get_frame_read().frame  
    img = cv2.resize(img, (400 , 400)) 
    cv2.imshow("Image", img) 
    
    cv2.waitKey(1) 

me.land()

print("Drone Landed")

print("Program Run Sucessfull")