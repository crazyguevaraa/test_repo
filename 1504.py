import RPi.GPIO as GPIO
import time
import numpy as np
#import matplotlib.pyplot as plt

DAC_list = (26,19,13,6,5,11,9,10)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_list, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.output(17,1)

def num2dec (value):
    bit_depth = 8
    N = bit_depth - 1
    p = 0
    X = []
    while N > 0:
        p = int(value / 2**N)
        if p==1:
            X.append(1)
            value -= 2**N
        else:
            X.append(0)
        N-=1
    X.append(value)
    return X


def lightNumber (number):
    global DAC_list
    GPIO.output(DAC_list, 0)
    array = num2dec (number)
    for j in range(len(DAC_list)):
        if int(array[7 - j]):
            GPIO.output(DAC_list[7 - j],1)

def first():

    while True:
        try:
            print("Enter value (-1 to exit): ")
            number = int(input())
            if number == -1:
                print("Exit from the program")
                GPIO.output(DAC_list,0)
                break
            if number > 255:
                print("Incorrect data")
            else:
                lightNumber (number)
                voltage = 3.29*(number/255)
                print(number, "=", voltage, "V")
        except ValueError:
            print("Incorrect data")

def second():
    while True:
            for number in range(0,255):
                lightNumber(number)
                time.sleep(0.001)
                if (GPIO.input(4) == 0):
                    voltage = 3.29*(number/255)
                    print(number, "=", voltage, "V")
                    break



def binary():
    numElem = 128
    point = 0
    while numElem >= 1 :
        lightNumber(int((point + numElem)/ 255))
        time.sleep(0.000001)
        if(GPIO.input(4) == 0):
            point = point + numElem
        numElem = int (numElem / 2)             
    voltage = 3.29*(point / 255)
    print(point, "=", voltage, "V")
    return point
try:
    GPIO.output(17,1)
    while True:
        binary()
finally:
    GPIO.output(DAC_list, 0)
    GPIO.output(17,0)
    GPIO.cleanup()