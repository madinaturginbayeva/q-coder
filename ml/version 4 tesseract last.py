#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import io
import os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import cv2
import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from pytesseract import pytesseract
from difflib import SequenceMatcher



def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    
    #split pdf file to multiple pds
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = 'diploma/{}_page_{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        #print('Created: {}'.format(output_filename))
        
    #convert pdf to png, because tesseracts workd only with png file 
    for page in range(pdf.getNumPages()):
        images = convert_from_path('diploma/{}_page_{}.pdf'.format(
            fname, page+1))
        for image in images:
            image.save('diploma/{}_page_{}.png'.format(fname, page+1),'PNG')
            image_name2 = 'diploma/{}_page_{}.png'.format(fname, page+1)
            
            #crop name or id
            img = Image.open(image_name2)
            student_id = img.crop((430, 0, 920, 276))
            student_id.save('diploma/student_{}.png'.format(page+1))
            img_cv = cv2.imread('diploma/student_{}.png'.format(page+1))
            student_id_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            student_id_text =pytesseract.image_to_string(student_id_rgb)
            
            if ( name_student_database = student_id_text):
                #tesseract converts handwriting to txx file 
                img_cv = cv2.imread(image_name2)
                img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
                new =pytesseract.image_to_string(img_rgb)
                true_answers = open('diploma/RightAnswers.txt').read()
                m = SequenceMatcher(None, new, true_answers) #insert mark
                mark = m.ratio()*1388 #insert mark

