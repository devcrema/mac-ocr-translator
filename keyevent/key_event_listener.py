from pynput import keyboard
from pynput.keyboard import Key

shortcut_combination = {Key.cmd: False, Key.shift: False, "1": False}


def check_shortcut(key: Key, pressed: bool) -> bool:
    try:
        if key.char == "1":
            shortcut_combination["1"] = pressed
    except AttributeError:
        if key == Key.cmd:
            shortcut_combination[Key.cmd] = pressed
        if key == Key.shift:
            shortcut_combination[Key.shift] = pressed
    for result in shortcut_combination.values():
        if not result:
            return False
    return True


def on_press(key):
    shortcut_pressed = check_shortcut(key, True)
    print("shortcut pressed")
    print(shortcut_pressed)


def on_release(key):
    check_shortcut(key, False)

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def listen():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
