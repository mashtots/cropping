#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np

fileName = list(range(78))

img = cv2.imread('0011.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(gray,kernel,iterations = 2)
kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(erosion,kernel,iterations = 2)

edged = cv2.Canny(dilation, 30, 50)

_, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rects = [cv2.boundingRect(cnt) for cnt in contours]
rects = sorted(rects,key=lambda  x:x[1],reverse=True)
print(rects)

i = -1
j = 1
y_old = 5000
x_old = 5000
for rect in rects:
    x,y,w,h = rect
    area = w * h

    if area > 8000 and area < 1200000:

        if (y_old - y) > 200:
            i += 1
            y_old = y

        if abs(x_old - x) > 300:
            x_old = x
            x,y,w,h = rect

            out = img[y+10:y+h-10,x+10:x+w-10]
            cv2.imwrite('cropped\\' + str(fileName[i]) + '_' + str(j) + '.jpg', out)

            j+=1

img = cv2.imread("001.jpg",)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

binary = cv2.bitwise_not(gray)

(_,contours,_) = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#print(contours)
for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    #print(box)
    if w<125 and w>115 and h<125 and h>115:
        out = img[y+10:y+h-10,x+10:x+w-10]
        cv2.imwrite('cropped\\' + str(x) + '_' + str(y) + '.jpg', out)
