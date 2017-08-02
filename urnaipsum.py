#!/usr/bin/env python3.5

import remote
from time import sleep

# vlc -I rc --no-osd --rc-host 127.1:8888


player = remote.VLC()

player.add("/home/dg/Downloads/big_buck_bunny.mp4")
player.play()
sleep(0.1)
player.x("f on")
sleep(5)

player.clear()
player.add("/home/dg/Downloads/echo-hereweare.mp4")
player.play()

while True:
    sleep(5)
    player.clear()
    player.add("/home/dg/Downloads/echo-hereweare.mp4")
    player.play()
