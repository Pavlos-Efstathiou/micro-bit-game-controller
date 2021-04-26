# Importing modules

from pynput.keyboard import Key, Controller
from threading import Thread
from keybinds import *
import serial
import sys
import os

def main():
    port = str(input("Serial port that's connected to your micro:bit:\n"))
    baud = 115200
    serial_port = serial.Serial(port) 
    serial_port.baudrate = baud
    keyboard = Controller()
    keybinds = [
            input("Key(s) that will be pressed when the A button is pressed:\n"),
            input("Key(s) that will be pressed when the B button is pressed:\n")
    ]
    last = 0

    # Creates a new thread which setups the keybinds
    setupThread = Thread(target = keybinds_setup(keybinds), args = (1, ))
    # Starts the thread
    setupThread.start()
    # Ensures that this thread has been terminated
    setupThread.join()

    print("Press CTRL+C to exit")
    
    is_str = list(map(lambda x: isinstance(x, str), keybinds))

    while True:
        # Reads the serial output of your micro:bit
        serial_output = int(serial_port.read());

        # Presses and releases keys based upon the serial output of your micro:bit
        if serial_output != 0:
            last = 1
        # This is the opposite of elegant code, but I don't think theres a better way of doing this
        if serial_output == 1:
            if is_str[0]:
                keyboard.type(keybinds[0])
            else:
                keyboard.press(keybinds[0])
        elif serial_output == 2:
            if is_str[1]:
                keyboard.type(keybinds[1])
            else:
                keyboard.press(keybinds[1])
        elif last != 0:
            if not is_str[0]:
                keyboard.release(keybinds[0])
            if not is_str[1]:
                keyboard.release(keybinds[1])
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