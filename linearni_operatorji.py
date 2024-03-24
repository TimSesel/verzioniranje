import cv2 as cv
import numpy as np

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
    pass

def filtriraj_sobel_smer(slika):
    pass

if __name__ == '__main__':
    slika = cv.imread("Lenna_(test_image).png")
    cv.imshow("Originalna slika")
    cv.waitKey(0)

    # --------------------------------- Konvolucija ---------------------------------
    x = 0.1
    jedro = np.array([[x, x, x], [x, x, x], [x, x, x]])
    konvolucirana_slika = konvolucija(slika.astype(np.float32) / 255.0, jedro.astype(np.float32))

    cv.imshow("Konvolucija", konvolucirana_slika)
    cv.waitKey(0)

    pass