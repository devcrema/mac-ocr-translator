import os

from PIL import Image
from pytesseract import pytesseract


def ocr(image_path):
    try:
        if not os.path.exists(image_path):
            return None
        result = pytesseract.image_to_string(Image.open(image_path), timeout=2, lang='eng').replace("\n", "")
        os.remove(image_path)
        return result
    except RuntimeError as timeout_error:
        # Tesseract processing is terminated
        print("failed image processing")
        pass
