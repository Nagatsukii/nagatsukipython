import numpy as numpy
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('Images\coins_Dutch_17_18_C_coins_obv.jpg')
img2 = cv2.imread('Images\coins_ChastanaCoin.jpg')

blurred_img = cv2.GaussianBlur(img1,(15,15),0, 0.02)

cv2.imshow('Image1', img1)
#cv2.imshow('Image2', img2)
cv2.imshow('BlurredImage', blurred_img)
cv2.waitKey()

