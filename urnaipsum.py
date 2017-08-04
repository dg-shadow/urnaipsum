#!/usr/bin/env python

import remote
from time import sleep, time
import serial
import threading
import os
import sys

# vlc -I rc --no-osd --rc-host 127.1:8888

path = os.path.dirname(os.path.realpath(sys.argv[0]))

background_file = path + "/background.mpeg"
background_length = 7*60

button_file = path + "/button.mov"
button_length = 2*60+33



port = "/dev/ttyUSB0"
baud = 9600

incoming = serial.Serial(port, baud, timeout=100)

mutex = threading.Lock()
button_state = False
player = remote.VLC()

def play(file_path):
    global player
    player.clear()
    player.add(file_path)
    player.play()

def listen_to_button():
    global button_state
    while True:
        message = incoming.readline()
        if message == "on\r\n":
            mutex.acquire()
            button_state = True
            mutex.release()

        elif message == "off\r\n":
            mutex.acquire()
            button_state = False
            mutex.release()


thread = threading.Thread(target=listen_to_button)
thread.start()

mode = "background"
started = time()

play(background_file)
sleep(1)
player.x("f on")

while True:
    if mode == "background":
        if time() - started > background_length:
            print "looping background"
            play(background_file)
            started = time()
        if button_state:
            print "starting button"
            mode = "button"
            play(button_file)
            started = time()
    else:
        if time() - started > button_length:
            print "end of button"
            play(background_file)
            mode = "background"
            started = time()
    sleep(0.1)
