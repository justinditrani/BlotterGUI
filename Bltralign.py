#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:42:22 2019

@author: jdt
"""
import RPi.GPIO as GPIO
import time, argparse
import Blt8r4kpinlist as pin

if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description='No arguements for align')
    parser.add_argument()
    args = parser.parse_args()
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin.blotter,GPIO.OUT)
    GPIO.setup(pin.plunger,GPIO.OUT)
    
    GPIO.output(pin.blotter,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(pin.blotter,GPIO.LOW)
    
GPIO.cleanup()