#!/usr/bin/env python

import remote
from time import sleep
import serial
import threading

# vlc -I rc --no-osd --rc-host 127.1:8888

port = "/dev/ttyUSB0"
baud = 9600

incoming = serial.Serial(port, baud, timeout=10)

mutex = threading.Lock()
button_state = 0

def listen_to_button():
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

def main():
    thread = threading.Thread(target=listen_to_button)
    thread.start()

    player = remote.VLC()

    player.add("/home/dg/Downloads/echo-hereweare.mp4")
    player.play()
    sleep(0.1)
    player.x("f on")
    sleep(5)

    player.clear()
    player.add("/home/dg/Downloads/big_buck_bunny.mp4")
    player.play()

while True:
    sleep(1)
    # player.clear()
    # player.add("/home/dg/Downloads/big_buck_bunny.mp4")
    # player.play()
