from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import sys

image_input = imread('image.jpg')
gamma = 1.04

def grayFilter(img, gamma):
  r,g,b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

  r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

  grayscale_image = r * r_const ** gamma + g * g_const ** gamma + b * b_const ** gamma

  return grayscale_image

plt.imshow(grayFilter(image_input, gamma), cmap=plt.cm.get_cmap('gray'))
plt.show()
