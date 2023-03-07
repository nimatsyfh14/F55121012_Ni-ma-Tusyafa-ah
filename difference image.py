import cv2

# membaca dua citra
img1 = cv2.imread('1.jpg')
img1 = cv2.resize(img1, (665, 400))
img2 = cv2.imread('2.jpg')
img2 = cv2.resize(img2, (665, 400))

# mengubah citra menjadi grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# mengurangi kedua citra
diff_img = cv2.absdiff(gray_img1, gray_img2)

# menampilkan citra hasil difference image
cv2.imshow('Hasil Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
