from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import sys

image_input = imread('teste.jpg')
gamma = 1.04

def grayFilter(img, gamma):
  r,g,b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

  r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

  grayscale_image = r * r_const ** gamma + g * g_const ** gamma + b * b_const ** gamma

  return grayscale_image

plt.imshow(grayFilter(image_input, gamma), cmap=plt.cm.get_cmap('gray'))
plt.savefig('grey_filter.jpg')

img = plt.imread('grey_filter.jpg')


filtro_veritical = [[ -1, -2, -1],
                    [  0,  0,  0],
                    [  1,  2,  1]]

filtro_horizontal = [[ -1, 0, 1],
                     [ -2, 0, 2],
                     [ -1, 0, 1]]

n,m,d = img.shape

bordas_verticais_horizontais = np.zeros_like(img)

for linha in range (3, n-2):
    for coluna in range(3, m-2):
        pixels_locais = img[linha-1:linha+2, coluna-1:coluna+2, 0]

        pixels_transformados_verticais = filtro_veritical*pixels_locais
        valor_vertical = (pixels_transformados_verticais.sum()+3)/6

        pixels_transformados_horizontais = filtro_horizontal*pixels_locais
        valor_horizontal = (pixels_transformados_horizontais.sum()+3)/6

        valor_da_borda = (valor_vertical**2 + valor_horizontal**2)**.5
        bordas_verticais_horizontais[linha, coluna] = [valor_da_borda]*3
bordas_verticais_horizontais = bordas_verticais_horizontais/bordas_verticais_horizontais.max()
plt.imshow(bordas_verticais_horizontais)
plt.savefig('sobel_filter.png')