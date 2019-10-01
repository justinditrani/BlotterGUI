#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:00:16 2019

@author: jdt
"""
import RPi.GPIO as GPIO
import time, argparse
import Blt8r4kpinlist as pin

if __name__=='__main__':

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin.blotter,GPIO.OUT)
    GPIO.setup(pin.plunger,GPIO.OUT)
    
    parser = argparse.ArgumentParser(description='Arguments for cleanprocess')
    parser.add_argument('--btime', help='Duration of blot', default = 5, type=float,required=True)
    args = parser.parse_args()

    GPIO.output(pin.blotter,GPIO.HIGH)
    time.sleep(args.btime)
    GPIO.output(pin.blotter,GPIO.LOW)
    GPIO.output(pin.plunger,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin.plunger,GPIO.LOW)
    
GPIO.cleanup()

