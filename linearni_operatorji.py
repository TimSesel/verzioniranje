import cv2 as cv
import numpy as np
import math

def konvolucija(slika, jedro):
    y_slika, x_slika = slika.shape[:2]
    y_jedro, x_jedro = jedro.shape[:2]
    nova_slika = slika

    for i in range(0, y_slika):
        for j in range(0, x_slika):
            nov_piksel = 0

            for k in range(0, y_jedro):
                for l in range(0, x_jedro):
                    if i+k < y_slika and j+l < x_slika:
                        nov_piksel += slika[i+k, j+l] * jedro[k, l]
                    elif i+k >= y_slika and j+l < x_slika:
                        nov_piksel += slika[i, j+l] * jedro[k, l]
                    elif i+k < y_slika and j+l >= x_slika:
                        nov_piksel += slika[i+k, j] * jedro[k, l]
                    else:
                        nov_piksel += slika[i, j] * jedro[k, l]

            nova_slika[i, j] = nov_piksel

    return nova_slika

def filtriraj_z_gaussovim_jedrom(slika, sigma):
    velikost_jedra = (int)(((2 * sigma) * 2) + 1)
    k = (velikost_jedra / 2) - 0.5
    jedro = np.zeros((velikost_jedra, velikost_jedra), dtype=np.float32)
    pod_enacba_1 = (1 / (2 * math.pi * (sigma ** 2))) * math.e
    pod_enacba_2 = 2 * (sigma ** 2)

    for i in range(0, velikost_jedra):
        pod_enacba_i = (i - k - 1) ** 2
        for j in range(0, velikost_jedra):
            pod_enacba_j = (j - k - 1) ** 2
            jedro[i, j] = pod_enacba_1 ** (-(pod_enacba_i + pod_enacba_j) / pod_enacba_2)

    return konvolucija(slika, jedro)

def filtriraj_sobel_horizontalno(slika):
    jedro = np.array([[1, 2, 1], [0, 0, 0], [-1, -2 -1]], dtype=np.float32)

    return konvolucija(slika, jedro)

if __name__ == '__main__':
    slika = cv.imread("Lenna_(test_image).png")
    cv.imshow("Originalna slika", slika)
    cv.waitKey(0)

    # --------------------------------- Konvolucija ---------------------------------
    x = 0.2
    y_jedro = 3
    x_jedro = 3
    jedro = np.full((y_jedro, x_jedro), x, dtype=np.float32)
    konvolucirana_slika = konvolucija(slika.copy().astype(np.float32) / 255.0, jedro)

    cv.imshow("Konvolucija", konvolucirana_slika)
    cv.waitKey(0)

    # --------------------------------- Gauss ---------------------------------
    sigma = 2.0
    gauss_slika = filtriraj_z_gaussovim_jedrom(slika.copy().astype(np.float32) / 255.0, sigma)

    cv.imshow("Gauss", gauss_slika)
    cv.waitKey(0)

    # --------------------------------- Sobel ---------------------------------
    sobel_slika = filtriraj_sobel_horizontalno(slika.copy().astype(np.float32) / 255.0)

    cv.imshow("Sobel", sobel_slika)
    cv.waitKey(0)

    pass