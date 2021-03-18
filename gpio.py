import time
from string import zfill
import RPi.GPIO as GPIO # importiruem chob rabotalo
#
GPIO.setmode(GPIO.BCM)  # numeraziya pinov
chan_list = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(chan_list, GPIO.OUT)

#def#
    
def GPIO_to_number(ledNumber):
    return chan_list[ledNumber]

def OffLight():
    for i in range (0, 8):
        GPIO.output(GPIO_to_number(i), 0)
    

def lightUp(ledNumber, period):
    ledNumber = GPIO_to_number(ledNumber)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)

def darkUp(ledNumber, period):
    ledNumber = GPIO_to_number(ledNumber)
    GPIO.output(ledNumber, 0)
    time.sleep(period)
    GPIO.output(ledNumber, 1)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)


def runningLight(count, period):
    for i in range(0, count):
        for j in range(0, 8):
            lightUp(j, period)

def runningDark(count, period):
    for i in range(0, 8):
        GPIO.output(GPIO_to_number(i), 1)
    for i in range(0, count):
        for j in range(0, 8):
            darkUp(j, period)

def decToBinList(decNumber):
    b = 1
    a = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1

    return a

def lightNumber(number):
    bin_list = decToBinList(number)
    for i in range (0, 8):
        GPIO.output(GPIO_to_number(i), bin_list[7 - i]) 
    time.sleep(1)
    OffLight()

def runningPattern(pattern, direction):
    lightNumber(pattern)
    if direction >= 0:
        lightNumber(pattern >> direction)
    else:
        lightNumber(pattern << abs(direction))
    OffLight()
    
    

            




#section code


ledNumber = int(input())
direction = int(input())
#decToBinList(ledNumber)
#blinkCount = int(input())
#linkPeriod = int(input())
#lightUp(ledNumber, period)
#runningDark(blinkCount, blinkPeriod)
runningPattern(ledNumber, direction)
OffLight()




    
