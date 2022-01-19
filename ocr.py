import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def image_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def image_array(image):
    image = np.array(image)
    image = image[..., :3]
    return image


def image_resize(image, scale):
    (width, height) = (image.width * scale, image.height * scale)
    return image.resize((width, height))


def get_text(screenxy, scale, psm, whitelist) -> str:
    screenshot = ImageGrab.grab(bbox=screenxy)
    resize = image_resize(screenshot, scale)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    return pytesseract.image_to_string(thresholding,
                                       config=f'--psm {psm} -c tessedit_char_whitelist={whitelist}').strip()


def get_text_image(image, whitelist) -> str:
    resize = image_resize(image, 3)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    return pytesseract.image_to_string(thresholding, config=f'--psm 7 -c tessedit_char_whitelist={whitelist}').strip()

