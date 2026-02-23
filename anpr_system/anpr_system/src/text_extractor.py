import easyocr
from .config import OCR_LANG

class TextExtractor:
    def __init__(self):
        self.reader = easyocr.Reader(OCR_LANG)

    def extract(self, plate_img):
        results = self.reader.readtext(plate_img)
        if results:
            return results[0][1].replace(" ", "")
        return None