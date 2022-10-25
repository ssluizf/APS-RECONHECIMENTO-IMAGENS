import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('grey_image.jpg')


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
        valor_vertical = (pixels_transformados_verticais.sum()+4)/8

        pixels_transformados_horizontais = filtro_horizontal*pixels_locais
        valor_horizontal = (pixels_transformados_horizontais.sum()+4)/8

        valor_da_borda = (valor_vertical**2 + valor_horizontal**2)**.5
        bordas_verticais_horizontais[linha, coluna] = [valor_da_borda]*3
bordas_verticais_horizontais = bordas_verticais_horizontais/bordas_verticais_horizontais.max()
plt.imshow(bordas_verticais_horizontais)
plt.savefig('sobel_filter.png')