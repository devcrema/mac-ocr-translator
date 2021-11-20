from pynput import keyboard
from pynput.keyboard import Key

shortcut_combination = {Key.cmd: False, Key.shift: False, "1": False}
is_processing = False


def check_shortcut(key: Key, pressed: bool) -> bool:
    global is_processing
    if is_processing and pressed:
        return False
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
            is_processing = False
            return False
    is_processing = True
    return True


def on_release(key):
    check_shortcut(key, False)


def listen(on_shortcut_triggered):
    def on_press(key):
        shortcut_pressed = check_shortcut(key, True)
        if shortcut_pressed:
            on_shortcut_triggered()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
