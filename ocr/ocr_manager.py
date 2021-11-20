from PIL import Image
from pytesseract import pytesseract


def ocr(image_path) -> str:
    try:
        return pytesseract.image_to_string(Image.open(image_path), timeout=2, lang='eng').replace("\n", "")
    except RuntimeError as timeout_error:
        # Tesseract processing is terminated
        print("failed image processing")
        pass
