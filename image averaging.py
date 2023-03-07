import cv2
import numpy as np

# membaca tiga citra
img1 = cv2.imread('1.jpg')
img1 = cv2.resize(img1, (665, 400))
img2 = cv2.imread('2.jpg')
img2 = cv2.resize(img2, (665, 400))

# mengubah citra menjadi grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# menghitung rata-rata nilai piksel
averaged_img = cv2.addWeighted(gray_img1, 1/3, gray_img2, 1/3, 0)

# menampilkan citra hasil image averaging
cv2.imshow('Hasil Image Averaging', averaged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
