# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:30:15 2018

@author: OMEN
"""

import cv2
import numpy as np


    #%%
def checkIfContains(outside, inside):        
    return (inside[0] > outside[0] and inside[0] + inside[2]  < outside[0] + outside[2] and inside[1] > outside[1] and inside[1] + inside[3] < outside[1] + outside[3])

def filterRectangles(rects):
    #Checks if each contour contains some other contous - neccesary to avoid
    #spotting two "0" inside of 8 etc.
    rects_filtered = []
    flag = 0
    for i in range(0, len(rects)):
        for j in range(0, len(rects)):
            if(checkIfContains(rects[j], rects[i])):
                flag = 1
                break
        if(flag == 0):
            rects_filtered.append(rects[i])
        else:
            flag = 0
    return rects_filtered


sample = cv2.imread('input//008.jpg')
white_image = np.zeros(sample.shape) + 255
I = cv2.resize(cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY), (700,600))
cv2.imshow("sample", I)



#%%
#using adaptive threshold binarization to make algorithm robust on affine brightness changes        
B = cv2.adaptiveThreshold(I,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('B', B)
median = B
#using median blur to reduce noise coming from adaptive threshold binarization
#number of iterations was determined experimentally based on sample images    
for i in range(0,7):
    median = cv2.medianBlur(median,3)
    #cv2.imshow('median', median)
    
img, ctr, hierarchy = cv2.findContours(B, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#filtering contours froms small, unimportant objects
ctr = list(filter(lambda el : el.shape[0]>70 and el.shape[0]<500, ctr))

for i in range(0,100):
    cv2.drawContours(white_image, ctr, -1, (0,0,255))
cv2.imshow("ctrs", white_image)    
#%%
rects = []
i=0
I_1 = B.copy()
for c in ctr:
    #getting bounding rectangle for detected digits
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    rect = (x, y, w, h) 
    rects.append(rect)
#        cv2.rectangle(I_1, (x, y), (x+w, y+h), (0, 255, 0), 1);
#        cv2.imshow("final",I_1)
filtered = filterRectangles(rects)
#%%

I_2 = B.copy()
for i in range(0, len(filtered)):
    cv2.rectangle(I_2, (filtered[i][0], filtered[i][1]), (filtered[i][0]+filtered[i][2], filtered[i][1]+filtered[i][3]), (0, 255, 0), 1);
cv2.imshow("filtered", I_2)   
#%%
i=0
resized = []
filtered.sort(key = lambda x: x[0])
for f in filtered:
#extracting and downscaling segmented digits to 28x28 in order to be compatible with MNIST database
    t = cv2.bitwise_not(median[f[1] - int(f[3]*0.1):f[1]+int(f[3]*1.1), f[0] - int(f[2]*0.1):f[0]+int(1.1*f[2])])
    resized = cv2.resize(t, (28,28))
    cv2.imwrite("output//0000" + str(i) + ".jpg", resized)
    i+=1

    


    