from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def basic_image_info(image_path):
    image = Image.open(image_path)
    info = {
        "format": image.format,
        "size": image.size,
        "mode": image.mode
    }
    return info