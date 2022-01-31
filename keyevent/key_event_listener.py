from pynput import keyboard
from pynput.keyboard import Key

from common.event_type import EventType

trans_shortcut_combination = {Key.cmd: False, Key.shift: False, "1": False}
pron_shortcut_combination = {Key.cmd: False, Key.shift: False, "2": False}
is_processing = False


def check_shortcut(key: Key, pressed: bool) -> EventType:
    global is_processing
    if is_processing and pressed:
        return EventType.NONE
    try:
        if key.char == "1":
            trans_shortcut_combination["1"] = pressed
        elif key.char == "2":
            pron_shortcut_combination["2"] = pressed
    except AttributeError:
        if key == Key.cmd:
            trans_shortcut_combination[Key.cmd] = pressed
            pron_shortcut_combination[Key.cmd] = pressed
            trans_shortcut_combination["1"] = False  # 숫자가 릴리즈되지 않는 이슈로 인해 추가
            pron_shortcut_combination["2"] = False  # 숫자가 릴리즈되지 않는 이슈로 인해 추가
        if key == Key.shift:
            trans_shortcut_combination[Key.shift] = pressed
            pron_shortcut_combination[Key.shift] = pressed
            trans_shortcut_combination["1"] = False  # 숫자가 릴리즈되지 않는 이슈로 인해 추가
            pron_shortcut_combination["2"] = False  # 숫자가 릴리즈되지 않는 이슈로 인해 추가
    print(trans_shortcut_combination)
    if all(trans_shortcut_combination.values()):
        return EventType.TRANSLATE
    if all(pron_shortcut_combination.values()):
        return EventType.PRONUNCIATION
    return EventType.NONE


def on_release(key):
    check_shortcut(key, False)


def listen(on_shortcut_triggered):
    def on_press(key):
        on_shortcut_triggered(check_shortcut(key, True))

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
