import sys
import os

sys.path.append(os.getcwd())

import linearni_operatorji
import numpy as np
import cv2 as cv

# Test bo izvršil funkcijo iz glavnega programa linearni_operatorji
# Če slika med konvolucijo spremeni dimenzije (slika.shape[:2]), bo test zaznal napako
def test():
    slika = cv.imread("Lenna_(test_image).png")
    x = 0.1
    y_jedro = 3
    x_jedro = 3
    jedro = np.full((y_jedro, x_jedro), x, dtype=np.float32)
    konvolucirana_slika = linearni_operatorji.konvolucija(slika.copy().astype(np.float32) / 255, jedro)
    np.testing.assert_array_equal(slika.shape[:2], konvolucirana_slika.shape[:2], err_msg='Slika je med konvolucijo premenila obliko!')