import time
import math
import numpy as np
import matplotlib.pyplot as plt
#from string import zfill
import RPi.GPIO as GPIO # importiruem chob rabotalo
#
GPIO.setmode(GPIO.BCM)  # numeraziya pinov
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(chan_list, GPIO.OUT)

    

def reverse(arr, n):
    r_arr = np.zeros(n)
    for i in range(n):
        r_arr[i] = arr[n - i - 1]
    return r_arr

def decToBinList(decNumber):
    bNumber = np.zeros(8)
    for j in range(8):
        bNumber[j] = int(decNumber % 2)
        decNumber = int(decNumber / 2)
    return reverse(bNumber, 8)

def num2dac(value):
    registers = decToBinList(value)
    for i in range(8):
        if registers[i] == 1:
            GPIO.output(chan_list[i], 1)
   
def hello():
    print ("Enter the number (-1 for exit):")
    value = int(input())
    while (value != -1):
        num2dac(value)
        value = int(input())
        GPIO.output(chan_list, 0) 

def HowAreYou():
    print ("enter how many times you want repetitions:")
    repetitionsNumber = abs(int(input()))
    while (repetitionsNumber != 0):
        repetitionsNumber = repetitionsNumber - 1
        for n in range(0, 255, 1):
            num2dac(n)
            time.sleep(0.05)
            GPIO.output(chan_list,0)
        for n in range(255, 0, -1):
            num2dac(n)
            time.sleep(0.05)
            GPIO.output(chan_list,0)    

try:
    hello()
    HowAreYou()
except (ValueError, Exception):
    print ("enter only number!!!")       
finally:
    GPIO.output(chan_list,0)
    GPIO.cleanup()    

    