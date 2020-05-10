#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import os
import os.path
import pytesseract
import argparse
import cv2
import time
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)
from PIL import Image

start_time = time.time()


def pdfToPng():
    path = '/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/pngFormat'
    path2 = '/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/Tesseract'
    try:
        os.mkdir(path, path2)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
    images = convert_from_path('diploma.pdf')

    for i, image in enumerate(images):
        fname = 'image'+str(i+1)+'.png'
        image.save('/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/pngFormat/'+fname, "PNG")

# Crops the image and saves it as "new_filename"
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

        #image_name = '/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/image1.png'
def check():  # The x, y coordinates of the areas to be cropped. (left, upper, right, lower)
    for i in range(83):
        path = '/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/image' + str(i + 1)
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)


    for i in range(1):
        crop_areas = [(0, 0, 920, 276), (1000, 100, 1600,270), (0, 280, 1650, 380), (0, 370, 1650, 530), (0, 520, 1650, 560)
            , (0, 550, 1650, 750), (0, 740, 1650, 805), (0, 800, 1650, 1300), (0, 1290, 1650, 1410), (0, 1400, 1650, 1580)
            , (0, 1580, 1655, 1730), (0, 1730, 1650, 2080)]

        for i in range(83):
            image_name = '/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/pngFormat/image' + str(i+1) +'.png'
            img = Image.open(image_name)
            image_name2 = '/Users/turginbaevamadina/PycharmProjects/diploma/diplCropToPng/image' + str(i + 1) + '.png'

            # Loops through the "crop_areas" list and crops the image based on the coordinates in the list
            for i, crop_area in enumerate(crop_areas):
                ...
                #if (i == 0):
                #   filename = os.path.splitext(image_name)[0]
                #   ext = os.path.splitext(image_name)[1]
                #   new_filename = filename +'/tensorflow'+ '_name' + str(
                #       i) + ext  # tanserflow - name of the second folder
                #   crop_image(img, crop_area, new_filename)
                #if (i == 1):
                #    filename = os.path.splitext(image_name)[0]
                #   ext = os.path.splitext(image_name)[1]
                #   new_filename = filename + '/tensorflow'+ '_name' + str(
                #       i) + ext  # tanserflow - name of the second folder
                #   crop_image(img, crop_area, new_filename)
                if (i == 3):
                    filename = os.path.splitext(image_name2)[0]
                    ext = os.path.splitext(image_name2)[1]
                    new_filename = filename + '/tensorflow'+ '_name' + str(
                        1) + ext  # tanserflow - name of the second folder
                    crop_image(img, crop_area, new_filename)
                if (i == 5):
                    filename = os.path.splitext(image_name2)[0]
                    ext = os.path.splitext(image_name2)[1]
                    new_filename = filename + '/tensorflow'+ '_name' + str(
                        2) + ext  # tanserflow - name of the second folder
                    crop_image(img, crop_area, new_filename)
                if (i == 7):
                    filename = os.path.splitext(image_name2)[0]
                    ext = os.path.splitext(image_name2)[1]

new_filename = filename + '/tensorflow'+ '_name' + str(
                        3) + ext  # tanserflow - name of the second folder
                    crop_image(img, crop_area, new_filename)
                if (i == 9):
                    filename = os.path.splitext(image_name2)[0]
                    ext = os.path.splitext(image_name2)[1]
                    new_filename = filename + '/tensorflow'+ '_name' + str(
                        4) + ext  # tanserflow - name of the second folder
                    crop_image(img, crop_area, new_filename)
                if (i == 11):
                    filename = os.path.splitext(image_name2)[0]
                    ext = os.path.splitext(image_name2)[1]
                    new_filename = filename + '/tensorflow'+ '_name' + str(
                        5) + ext  # tanserflow - name of the second folder
                    crop_image(img, crop_area, new_filename)


def tesseract():
    #reader = PdfFileReader('/Users/turginbaevamadina/Downloads/diploma.pdf', 'r')
    #sum = reader.getNumPages()
    img_cv = cv2.imread(r'tensorflow_name2.png')

    # By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
    # we need to convert from BGR to RGB format/mode:
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img_rgb))
    # OR
    img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
    print(pytesseract.image_to_string(img_rgb))



#pdfToPng()
#check()
tesseract()
print("--- %s seconds ---" % (time.time() - start_time))

