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

# Importing modules

import serial
import sys
import os
from pynput.keyboard import Key, Controller
from threading import Thread
from keybinds import *

def main(): 
    print("Press ctrl+c exit")
    port = str(input("Serial port that's connected to your micro:bit:\n"))
    baud = 115200
    serial_port = serial.Serial(port) 
    serial_port.baudrate = baud
    keyboard = Controller()
    keybinds = [input("key that will be pressed when the A button is pressed:\n"), input("Key that will be pressed when the B button is pressed:\n")]
    last = 0

    # Creates a new thread which setups the keybinds
    threading = Thread(target = keybinds_setup(keybinds, special_keys), args = (10, ))
    # Starts the thread
    threading.start()
    # Ensures that this thread has been terminated
    threading.join()

    while True:
        # Reads the serial output of your micro:bit
        serial_output = int(serial_port.read());

        # Presses and releases keys based upon the serial output of your micro:bit
        if serial_output != 0:
            last = 1
        if serial_output == 1:
            keyboard.press(keybinds[0])
        elif serial_output == 2:
            keyboard.press(keybinds[-1])
        elif last != 0:
            keyboard.release(keybinds[0])
            keyboard.release(keybinds[-1])
            last = 0

if __name__ == "__main__":
    # Tries to execute the main function
    try:
        main()
    # If a KeyboardInterrupt (^c) gets detected this script stops
    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)