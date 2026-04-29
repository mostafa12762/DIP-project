import cv2
import numpy as np
from scipy import stats

img_color = cv2.imread("image.jpg")  
img_gray = cv2.imread("image.jpg", 0)

# =========================
# Task 1 : Point Operations
# =========================
def addition(img, value):
    return cv2.add(img, np.ones(img.shape, dtype=np.uint8) * value)

def subtraction(img, value):
    return cv2.subtract(img, np.ones(img.shape, dtype=np.uint8) * value)

def division(img, value):
    return np.clip(img / value, 0, 255).astype(np.uint8)

def complement(img):
    return 255 - img

# =========================
# Task 4 : Neighborhood Processing
# =========================
def average_filter(img):
    return cv2.blur(img, (3,3))

def laplacian_filter(img):
    lap = cv2.Laplacian(img, cv2.CV_64F)
    return np.uint8(np.absolute(lap))

def max_filter(img):
    return cv2.dilate(img, np.ones((3,3), np.uint8))

def min_filter(img):
    return cv2.erode(img, np.ones((3,3), np.uint8))

def median_filter(img):
    return cv2.medianBlur(img, 3)

def mode_filter(image):
    padded = np.pad(image, 1, mode='edge')
    result = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded[i:i+3, j:j+3].flatten()
            mode_value = stats.mode(window, keepdims=True).mode[0]
            result[i, j] = mode_value

    return result


# Point Operations Results
added_image = addition(img_color, 50)
subtracted_image = subtraction(img_color, 50)
divided_image = division(img_color, 2)
complement_image = complement(img_color)

# Neighborhood Processing Results
average_filtered_image = average_filter(img_gray)
laplacian_filtered_image = laplacian_filter(img_gray)
maximum_filtered_image = max_filter(img_gray)
minimum_filtered_image = min_filter(img_gray)
median_filtered_image = median_filter(img_gray)
mode_filtered_image = mode_filter(img_gray)
