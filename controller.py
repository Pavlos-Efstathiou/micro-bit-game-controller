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
Packages to install: pip install pynput
"""

import serial
import sys
import os
from pynput.keyboard import Key, Controller

def main():
    port = "COM3" # This will certainly be different on your machine ex. "COM16"
    baud = 115200
    s = serial.Serial(port) # Don't know what to name this variable
    s.baudrate = baud
    keyboard = Controller()
    keybinds = [input("Key that will be pressed when the A button is pressed:\n"), input("Key that will be pressed when the B button is pressed:\n")]
    last = 0

    if keybinds[0] == "" or keybinds[1] == "" or keybinds[0] == None or keybinds[1] == None:
        print("Keybinds not setup, will use default keybinds")
        keybinds = ["d", Key.space]
    else:
        for i in range(len(keybinds)):
            if type(keybinds[i]) is float:
                print("Float Keybinds invalid")
                sys.exit();
            if keybinds[i] == "space":
                keybinds[i] = Key.space
                print("space = Key.space")
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
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
