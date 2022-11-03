from matplotlib.image import imread
import matplotlib.pyplot as plt
from Grey_Filter import *
from Sobel_Filter import *

image_input = imread('teste.jpg')
gamma = 1.04

image_gray = greyFilter(image_input, gamma)
plt.imsave('grey_filter.jpg', image_gray, cmap=plt.cm.get_cmap('gray'))


img = plt.imread('grey_filter.jpg')

bordas_verticais_horizontais = sobelFilter(img)

plt.imsave('sobel_filter.jpg', bordas_verticais_horizontais)
