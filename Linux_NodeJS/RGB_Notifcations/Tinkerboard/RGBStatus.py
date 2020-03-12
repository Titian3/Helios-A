import ASUS.GPIO as GPIO
import unittest   
import time
import sys
from random import randint

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv[1])
colorArg = str(sys.argv[1])
speedArg = int(sys.argv[2])
timeArg = int(sys.argv[3])
#Color pins
RED = 187
BLUE = 188
GREEN = 223

GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

pwmGREEN = GPIO.PWM(GREEN, 100)
pwmRED = GPIO.PWM(RED, 100)
pwmBLUE = GPIO.PWM(BLUE, 100)

pwmGREEN.start(0)
pwmRED.start(0)
pwmBLUE.start(0)

green = [100,0,0]
red = [0,100,0]
blue = [0,0,100]
blueStr = "blue"


purple = [0,100,100]
yellow = [100,100,0]
cyan = [100,0,100]
orange = [35,100,0]

white = [100,100,100]
colors = [green,red,blue,purple,yellow,cyan,orange,white]

speed = speedArg

if colorArg == "blue":
        selectedColor = blue
if colorArg == "green":
        selectedColor = green
if colorArg == "red":
        selectedColor = red
if colorArg == "purple":
        selectedColor = purple
if colorArg == "yellow":
        selectedColor = yellow
if colorArg == "cyan":
        selectedColor = cyan
if colorArg == "orange":
        selectedColor = orange
if colorArg == "white":
        selectedColor = white
if colorArg == "cycle":
        for z in range(0,8,1):
                selectedColor = colors[z]

#selectedColor = red
try:
	count = 0
	while count < timeArg:
		count = count + 1
                #Choose Color
                print "RGB Ready"
                greenFreqvalue = selectedColor[0]
                redFreqvalue = selectedColor[1]
                blueFreqvalue = selectedColor[2]
                

                print "Engage RGB"
                for i in range(0,100,speed):
                        if i < greenFreqvalue:
                                pwmGREEN.ChangeDutyCycle(i)
                        if i < redFreqvalue:
                                pwmRED.ChangeDutyCycle(i)
                        if i < blueFreqvalue:
                                pwmBLUE.ChangeDutyCycle(i)
                        time.sleep(0.02)
                print "Fade RGB"
                for i in range(100,-1,-speed):
                        if i < greenFreqvalue:
                                pwmGREEN.ChangeDutyCycle(i) 
                        if i < redFreqvalue:
                                pwmRED.ChangeDutyCycle(i)
                        if i < blueFreqvalue:
                                pwmBLUE.ChangeDutyCycle(i)
                        time.sleep(0.02)
                time.sleep(0.1)
                        
                
except KeyboardInterrupt:
	print "Key Stoping lights"
        pass
	pwmGREEN.stop()
        pwmRED.stop()
        pwmBLUE.stop()
	GPIO.cleanup()
finally:
	print "Fin - Stoping lights"
        pass
	pwmGREEN.stop()
        pwmRED.stop()
        pwmBLUE.stop()
	GPIO.cleanup()