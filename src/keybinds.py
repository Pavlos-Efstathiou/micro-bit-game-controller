from pynput.keyboard import Key
from printy import printy
from monad import Failure  # Don't worry i'll use this later

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
    "up arrow": Key.up,
}


# Function which sets up the keybinds
def keybinds_setup(keys):
    # No one likes nested for loops but this has to be done :(
    for i in range(len(keys)):
        if keys[i] == "":
            current_button = "A" if i == 0 else "B"
            button_string = f"[kB{{r}}]Warning:\nThe {current_button} button is not mapped to any key(s)!@"
            printy(button_string)
        for k, v in special_keys.items():
            if isinstance(keys[i], str) and keys[i] == k:
                keys[i] = v
