import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    y_slika, x_slika = slika.shape
    y_jedro, x_jedro = jedro.shape
    nova_slika = slika

    for i in range(0, y_slika - y_jedro + 1):
        for j in range(0, x_slika - x_jedro + 1):
            nov_piksel = 0

            for k in range(0, y_jedro):
                for l in range(0, x_jedro):
                    nov_piksel += slika[i+k, j+l] * jedro[k, l]

            nova_slika[i, j] = nov_piksel

    return nova_slika

def filtriraj_z_gaussovim_jedrom(slika, sigma):
    pass

def filtriraj_sobel_smer(slika):
    pass

if __name__ == '__main__':
    slika = cv.imread("Lenna_(test_image).png")
    cv.imshow("Originalna slika", slika)
    cv.waitKey(0)

    # --------------------------------- Konvolucija ---------------------------------
    x = 1.0
    jedro = np.array([[x, x, x], [x, x, x], [x, x, x]])
    konvolucirana_slika = konvolucija(slika.astype(np.float32), jedro.astype(np.float32))

    cv.imshow("Konvolucija", konvolucirana_slika)
    cv.waitKey(0)

    pass