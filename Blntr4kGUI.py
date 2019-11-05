#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:40:33 2019

@author: jdt
"""
from guizero import App, TextBox, Text, PushButton, CheckBox
from subprocess import call

def powerup():
    print("Power up")
    arguments = ["python3","Bln8r4kpowerupdown.py","--updown","up"]
    rc = call(arguments)
    button_timed.enable()
    button_user.enable()
    button_align.enable()
    
def powerdown():
    print("Power down")
    arguments = ["python3","Bln8r4kpowerupdown.py","--updown","down"]
    call(arguments)
    button_timed.disable()
    button_user.disable()
    button_align.disable()

def timed():
    print("starting process")
    blottime = str(float(stime.value))
    arguments = ["python3","Bltrtimedrun.py","--btime",blottime]
    call(arguments)
    button_user.disable()
    button_timed.disable()
    button_align.disable()
    
def userin():
    print("Power down")
    arguments = ["python3","Bltruserrun.py"]
    call(arguments)
    button_user.disable()
    button_timed.disable()
    button_align.disable()
    
def align():
    print("Power down")
    arguments = ["python3","Bltralign.py"]
    call(arguments)
    button_user.disable()
    button_timed.disable()
    button_align.disable()

app = App(title="Blottinator4000", layout="grid")
button_up   = PushButton(app, command=powerup,text="Ready", grid=[0,1])
button_down = PushButton(app, command=powerdown, text="Abort", grid=[1,1])
button_align= PushButton(app, command=align, text="Align the blotting pad using the XYZ stage", grid=[0,2])
button_timed= PushButton(app, command=timed, text="Pre defined blotting time", grid=[0,3])
button_user = PushButton(app, command=userin, text="Blot until user input", grid=[0,4])

stimelabel  = Text(app, text="Blot time (s)", grid=[1,3])
stime       = TextBox(app, grid=[2,3], text="5")

button_up.bg="yellow"
button_down.bg = "red"
button_timed.disable()
button_user.disable()
button_align.disable()

app.display()