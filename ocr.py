# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @anthony5301
# Modified by the-user-created on 21/10/2023
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


def get_bbox_of_portal_vote() -> tuple:
    minimum_text_area = 6500  # Minimum area to filter small noise

    # Get a screenshot of all the vote buttons, convert it to RGB,
    # and turn it into an array (so it can be processed by cv2)
    # bbox=(left, top, right, bottom)
    img = np.array(ImageGrab.grab(bbox=(166, 310, 520, 900)).convert("RGB"))

    # Convert the image to grayscale for better contour detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables to store bounding box coordinates of the extracted region
    extracted_x, extracted_y, extracted_w, extracted_h = 0, 0, 0, 0

    # Iterate through the contours and filter based on size (area)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / h  # Calculate the aspect ratio (width / height)

        # Filter rectangles based on the aspect ratio and area
        if w * h > minimum_text_area and aspect_ratio > 5:  # Customize the aspect ratio threshold as needed
            # Store the coordinates of the extracted rectangle
            extracted_x, extracted_y, extracted_w, extracted_h = x, y, w, h

            # Draw rectangles around the detected text regions (optional, for debugging purposes)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save image to disk for debugging purposes (optional)
    # cv2.imwrite("temp_files/test.png", img)

    # Adjust the bounding box coordinates to the original image (center of the vote button)
    extracted_x += 166
    extracted_y += 310

    return extracted_x, extracted_y, extracted_w, extracted_h
