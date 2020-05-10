#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

from PIL import Image

# Crops the image and saves it as "new_filename"
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)

for i in range(1):
    
    crop_areas = [(0, 0, 920, 276),(0, 0, 326,100)] #cut zadachi
    image_name = 'check'+ str(i) + '.png'
    img = Image.open(image_name)

        # Loops through the "crop_areas" list and crops the image based on the coordinates in the list
    for i, crop_area in enumerate(crop_areas):

        if(i==0):
            filename = os.path.splitext(image_name)[0]
            ext = os.path.splitext(image_name)[1]
            new_filename = 'tensorflow/'+filename + '_name' + str(i) + ext #tanserflow - name of the second folder
            crop_image(img, crop_area, new_filename)
        if(i==1):
            filename = os.path.splitext(image_name)[0]
            ext = os.path.splitext(image_name)[1]
            new_filename = 'tensorflow/'+filename + '_name' + str(i) + ext  #tanserflow - name of the second folder
            crop_image(img, crop_area, new_filename)

