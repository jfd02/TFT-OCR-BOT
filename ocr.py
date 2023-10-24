"""
Contains all code related to turning a screenshot into a string
"""

from typing import Any
import cv2
import numpy as np
from PIL import ImageGrab, Image
from tesserocr import PyTessBaseAPI, RIL
import settings
from vec4 import Vec4, GameWindow

TESSDATA_PATH = settings.TESSERACT_TESSDATA_PATH

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
    with PyTessBaseAPI(path=TESSDATA_PATH) as api:
        api.SetVariable("tessedit_char_whitelist", whitelist)
        api.SetPageSegMode(psm)
        api.SetImageBytes(thresholding.tobytes(), thresholding.shape[1], thresholding.shape[0], 1,
                          thresholding.shape[1])
        text = api.GetUTF8Text()
    return text.strip()


def get_text_from_image(image: ImageGrab.Image, whitelist: str = "") -> str:
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


def get_coordinates_of_text(screenxy: tuple, scale: int, psm: int, whitelist: str = "") -> list[Vec4]:
    screenshot = ImageGrab.grab(bbox=screenxy)
    resized_screenshot = image_resize(screenshot, scale)
    # data=pytesseract.image_to_boxes(resized_screenshot)
    # Don't instantiate lists like this: coordinates = [Vec4]
    coordinates = []
    with PyTessBaseAPI(path=tessdata_path) as api:
        api.SetImage(resized_screenshot)
        api.SetVariable("tessedit_char_whitelist", whitelist)
        api.SetPageSegMode(psm)
        boxes = api.GetComponentImages(RIL.TEXTLINE, True)
        # print(f'  Found {len(boxes)} text-line image components.')
        for i, (im, box, _, _) in enumerate(boxes):
            # im is a PIL image object
            # box is a dict with x, y, w and h keys
            api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
            ocr_result = api.GetUTF8Text()
            conf = api.MeanTextConf()
            print(f"  Box[{i}]: x={box['x']}, y={box['y']}, w={box['w']}, h={box['h']}, "
                  f"confidence: {conf}, text: {ocr_result}")
            area_of_text = Vec4(GameWindow(box['x'], box['y'], box['x'] + box['w'], box['y'] + box['h']))
            coordinates.append(area_of_text)
    return coordinates
