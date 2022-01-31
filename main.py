#!/usr/bin/env python3

import pyperclip

from common.event_type import EventType
from dialog.dialog_manager import show, show_text
from keyevent.key_event_listener import listen
from ocr.ocr_manager import ocr
from pronunciation import pronunciation_manager
from screencapture.screen_capture_manager import capture_screen
from translator.google_translator import translate

config = {"copy_to_clipboard": False}


def on_shortcut_triggered(event_type):
    if event_type == EventType.NONE:
        return
    image_path = capture_screen()
    text = ocr(image_path)
    if text is None:
        return
    if config["copy_to_clipboard"]:
        pyperclip.copy(text)
    trans_result = translate(text)
    if event_type == EventType.TRANSLATE:
        show(text, trans_result)
    elif event_type == EventType.PRONUNCIATION:
        show_text(pronunciation_manager.get_pronunciation(text))


if __name__ == '__main__':
    listen(on_shortcut_triggered)
