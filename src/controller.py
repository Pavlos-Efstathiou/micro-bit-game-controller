# Copyright (c) 2021 Pavlos Efstathiou
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Requires Python 3 or later
Packages to install:
pip install pynput
pip install pyserial
"""

import serial
import sys
import os
from pynput.keyboard import Key, Controller
from threading import Thread
from time import sleep


def keybinds_setup(keys, special):
    # print("Thread started")
    for i in range(len(keys)):
        if keys[i] == "" or keys[i] == None:
            print("Keybinds not setup, will use default keybinds")
            keys = ["d", Key.space]
        for k, v in special.items():
            if keys[i] == k:    
                keys[i] = v
    # print("Thread finished function")

def main():
    special_keys = {
        "alt": Key.alt,
        "alt gr": Key.alt_gr,
        "left alt": Key.alt_l,
        "right alt": Key.alt_r,
        "caps lock": Key.caps_lock,
        "ctrl": Key.ctrl,
        "left ctrl": Key.ctrl_l,
        "right ctrl": Key.ctrl_r,
        "delete": Key.delete,
        "down arrow": Key.down,
        "end": Key.end,
        "f1": Key.f1,
        "f2": Key.f2,
        "f3": Key.f3,
        "f4": Key.f4,
        "f5": Key.f5,
        "f6": Key.f6,
        "f7": Key.f7,
        "f8": Key.f8,
        "f9": Key.f9,
        "f10": Key.f10,
        "f11": Key.f11,
        "f12": Key.f12,
        "left arrow": Key.left,
        "right arrow": Key.right,
        "shift": Key.shift,
        "left shift": Key.shift_l,
        "right shift": Key.shift_r,
        "space": Key.space,
        "tab": Key.tab,
        "up arrow": Key.up
    }
    port = str(input("Serial port that's connected to your micro:bit:\n"))
    # if os.name == "posix":
    #     port = f"/dev/ttySUSB{port}/"
    # elif os.name == "nt":
    #     port = f"COM{port}"
    baud = 115200
    s = serial.Serial(port) # Don't know what to name this variable
    s.baudrate = baud
    keyboard = Controller()
    keybinds = [input("Key that will be pressed when the A button is pressed:\n"), input("Key that will be pressed when the B button is pressed:\n")]
    last = 0

    threading = Thread(target = keybinds_setup(keybinds, special_keys), args = (10, ))
    threading.start()
    threading.join()

    while True:
        serial_output = int(s.read());
        if serial_output != 0:
            last = 1
        if serial_output == 1:
            keyboard.press(keybinds[0])
        elif serial_output == 2:
            keyboard.press(keybinds[1])
        elif last != 0:
            keyboard.release(keybinds[0])
            keyboard.release(keybinds[1])
            last = 0
if __name__ == "__main__":
    try:
        os.system("title Micro:bit Game controller")
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
