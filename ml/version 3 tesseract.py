#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def pdfToPng():
    path = 'png'
    inputpdf = PdfFileReader(open("diploma.pdf", "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("png/student%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
        input_path = "png/student%s.pdf" % i
        output_name = "png/student%s.png" % i
        source = Image(filename=input_path, resolution=300, width=2200)
        images = source.sequence
        for i in range(len(images)):
            Image(images[0]).save(filename=output_name.format(i))
        image_name2 = output_name
        img_cv = cv2.imread(image_name2)
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        new =pytesseract.image_to_string(img_rgb)
        file1 = open("png/student_text%s.png" % i,"a")
        file1.write(new)
        file1.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
from wand.image import Image

