from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('smallgold.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

cv2.imwrite('smallgoldgray.png', img_gray)