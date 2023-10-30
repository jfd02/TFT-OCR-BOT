# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @anthony5301
# Modified by the-user-created
#

"""
Contains all code related to turning a screenshot into a string
"""

from typing import Any
import cv2
import numpy as np
from PIL import ImageGrab, Image
from tesserocr import PyTessBaseAPI
import settings
import platform

if platform.system() == 'Darwin':
    TESSDATA_PATH = settings.TESSERACT_TESSDATA_PATH_OSX
else:
    TESSDATA_PATH = settings.TESSERACT_TESSDATA_PATH

ALPHABET_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROUND_WHITELIST = "0123456789-"
PORTAL_WHITELIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-"


def image_grayscale(image: Image) -> Any:
    """Converts an image to grayscale so OCR has an easier time deciphering characters"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_thresholding(image: Image) -> Any:
    """Applies thresholding to the image https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html"""
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def image_array(image: Image) -> Any:
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
    with PyTessBaseAPI(path=TESSDATA_PATH) as api:
        api.SetVariable("tessedit_char_whitelist", whitelist)
        api.SetPageSegMode(psm)
        api.SetImageBytes(thresholding.tobytes(), thresholding.shape[1], thresholding.shape[0], 1,
                          thresholding.shape[1])
        text = api.GetUTF8Text()
    return text.strip()


def get_text_from_image(image: Image, whitelist: str = "") -> str:
    """Takes an image and returns the text"""
    resize = image_resize(image, 3)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    with PyTessBaseAPI(path=TESSDATA_PATH) as api:
        api.SetVariable("tessedit_char_whitelist", whitelist)
        api.SetPageSegMode(7)
        api.SetImageBytes(thresholding.tobytes(), thresholding.shape[1], thresholding.shape[0], 1,
                          thresholding.shape[1])
        text = api.GetUTF8Text()
    return text.strip()


def find_template_centers(template_path: str, threshold: float,
                          region: tuple[int, int, int, int]) -> list[tuple[int, int]]:
    """Finds template centers within the specified region of the screen."""
    image = np.array(ImageGrab.grab(bbox=region).convert("L"))
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, thresholded_result = cv2.threshold(result, threshold, 1, cv2.THRESH_BINARY)
    locations = cv2.findNonZero(thresholded_result)

    centers = []
    if locations is not None:
        for loc in locations:
            x, y = loc[0]
            h, w = template.shape
            center_x = x + w // 2
            center_y = y + h // 2
            centers.append((center_x, center_y))

    return filter_centers(centers)


def filter_centers(centers, min_distance_squared=100) -> list[tuple[int, int]]:
    """Filters the centers to remove duplicates"""
    filtered_centers = set()
    for center in centers:
        if not any(np.sum((np.array(center) - np.array(filtered_center)) ** 2) < min_distance_squared
                   for filtered_center in filtered_centers):
            filtered_centers.add(center)
    return list(filtered_centers)
