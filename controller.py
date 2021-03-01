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
keybinds = [str(input("Key that will be pressed when the A button is pressed:\n")), input("Key that will be pressed when the B button is pressed:\n")]
last = 0

if keybinds[0] == "" or keybinds[1] == "":
    print("Config file not setup will use default keybinds")
    keybinds = ["d", Key.space]
else:
    for i in range(len(keybinds)):
        if keybinds[i] == "space":
            print()
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