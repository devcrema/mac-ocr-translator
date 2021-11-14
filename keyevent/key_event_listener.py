from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def listen():
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
