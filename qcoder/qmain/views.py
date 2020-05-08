from django.shortcuts import render, redirect
from .models import Course, Student
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from users.models import Teacher, Student

import os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import cv2
from PyPDF2 import PdfFileWriter, PdfFileReader
from pytesseract import pytesseract
import io 
pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'



def main(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            if group.name == 'Teacher':
                    Teacher.objects.create(user=user)
            elif group.name == 'Student':
                    Student.objects.create(user=user)
            user.groups.add(group)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'qmain/landing.html', {'form': form})

def courses(request):
    context = {
        'courses' : Course.objects.all(),
        'title' : 'Courses'
    }
    return render(request, 'qmain/courses.html', context)

def assignments(request):
    return render(request, 'qmain/assignments.html', {'title':'Assignments'})

def students(request):
    return render(request, 'qmain/students.html', {'title':'Student'})

def course(request):
    return render(request, 'qmain/course.html', {'title':'Course'})



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
        print('Created: {}'.format(output_filename))
        
    #convert pdf to png, because tesseracts workd only with png file 
    for page in range(pdf.getNumPages()):
        images = convert_from_path('diploma/{}_page_{}.pdf'.format(
            fname, page+1))
        for image in images:
            image.save('diploma/{}_page_{}.png'.format(fname, page+1),'PNG')
            image_name2 = 'diploma/{}_page_{}.png'.format(fname, page+1)
            
            #tesseract converts handwriting to txx file 
            img_cv = cv2.imread(image_name2)
            img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            new =pytesseract.image_to_string(img_rgb)
            file1 = io.open('diploma/{}_page_{}.txt'.format(fname, page+1),"a",encoding="utf-8")
            file1.write(new)
            file1.close()