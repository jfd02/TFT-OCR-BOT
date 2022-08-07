"""
Contains all code related to turning a screenshot into a string
"""

from typing import Any
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
import settings

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_PATH


ALPHABET_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROUND_WHITELIST = "0123456789-"


def image_grayscale(image: ImageGrab.Image) -> Any:
    """Converts an image to grayscale so OCR has an easier time deciphering characters"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_thresholding(image: ImageGrab.Image) -> Any:
    """Applies thresholding to the image https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html"""
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def image_array(image: ImageGrab.Image) -> Any:
    """Turns the image into an array"""
    image = np.array(image)
    image = image[..., :3]
    return image


def image_resize(image: int, scale: int) -> Any:
    """Resizes the image using the scale passed in argument two"""
    (width, height) = (image.width * scale, image.height * scale)
    return image.resize((width, height))


def get_text(screenxy: tuple, scale: int, psm: int, whitelist: str = "") -> str:
    """Returns text from screen coordinates"""
    screenshot = ImageGrab.grab(bbox=screenxy)
    resize = image_resize(screenshot, scale)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    return pytesseract.image_to_string(thresholding,
                                       config=f'--psm {psm} -c tessedit_char_whitelist={whitelist}').strip()


def get_text_from_image(image: ImageGrab.Image, whitelist: str = "") -> str:
    """Takes an image and returns the text"""
    resize = image_resize(image, 3)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    return pytesseract.image_to_string(thresholding,
                                       config=f'--psm 7 -c tessedit_char_whitelist={whitelist}').strip()
