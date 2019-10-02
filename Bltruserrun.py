#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:25:39 2019

@author: jdt
"""

import RPi.GPIO as GPIO
import time, argparse
import Blt8r4kpinlist as pin

if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description='No arguements for human blot')
    parser.add_argument()
    args = parser.parse_args()
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin.blotter,GPIO.OUT)
    GPIO.setup(pin.plunger,GPIO.OUT)
    
    while True:
        i = input("Press ender to start blotting")
        if not i:
            break
        print("Your input:", i)
    print("Blotting in 3 seconds")
    
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    
    while True:
        GPIO.output(pin.blotter,GPIO.HIGH)
        i = input("Press ender to stop blotting")
        if not i:
            break
        print("Your input:", i)
    
    GPIO.output(pin.blotter,GPIO.LOW)
    GPIO.output(pin.plunger,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin.plunger,GPIO.LOW)
    
GPIO.cleanup()