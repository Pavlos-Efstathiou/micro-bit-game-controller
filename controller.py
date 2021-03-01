"""
This requires Python 3 or later
Packages to install: pip install pynput
"""
import serial
from pynput.keyboard import Key, Controller
port = "COM3" # This will certainly be different on your machine ex. "COM16"
baud = 115200
s = serial.Serial(port) # Don't know what to name this variable
s.baudrate = baud
 
keyboard = Controller()
 
last = 0
 
while 1:
    serial_output = int(s.read());
    if serial_output != 0:
        last = 1
    if serial_output == 1:
        keyboard.press("d")
    elif serial_output == 2:
        keyboard.press(Key.space)
    elif last != 0:
        keyboard.release("d")
        keyboard.release(Key.space)
        last = 0
