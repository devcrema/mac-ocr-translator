#!/usr/bin/env python3

# Raycast Script Command Template
#
# Duplicate this file and remove ".template." from the filename to get started.
# See full documentation here: https://github.com/raycast/script-commands
#
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title ocr-translator
# @raycast.mode compact
#
# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName ocr-translator

import subprocess
import sys
import pkg_resources

required = {'pynput', 'pytesseract', 'Pillow', 'pyperclip', 'googletrans', 'pysle'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

subprocess.call(["python3", "./main.py"])
