from django.shortcuts import render, redirect
from .models import Course, Student, Task
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from users.models import Teacher, Student
from .forms import CourseForm
import os
import io 
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import cv2
from PyPDF2 import PdfFileWriter, PdfFileReader
from pytesseract import pytesseract
from difflib import SequenceMatcher
from PIL import Image
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

@login_required
def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            print('YES')
            course = form.save()
            course.lector = Teacher.objects.get(user = request.user)
            course.save()
        else:
            print('NO')

    try:
        courses = Course.objects.filter(lector=Teacher.objects.get(user = request.user))
    except Course.DoesNotExist:
        courses = None
    context = {
        'courses' : courses,
        'title' : 'Courses',
        'form': CourseForm(),
        'user_is_teacher': is_member(request.user)
    }
    return render(request, 'qmain/courses.html', context)

def is_member(user):
    return user.groups.filter(name='Teacher').exists()

@login_required
def assignments(request):
    return render(request, 'qmain/assignments.html', {'title':'Assignments'})
@login_required
def students(request):
    return render(request, 'qmain/students.html', {'title':'Student'})
@login_required
def course(request, id):
    tasks = Task.objects.filter(course_id=Course.objects.get(id=id))
    return render(request, 'qmain/course.html', {'title':'Tasks', 'tasks':tasks, 'course_id':course_id})

@login_required
def check_exam(request):
    if request.method == 'POST':
        path = 'media/diploma.pdf'
        fname = os.path.splitext(os.path.basename(path))[0]
        pdf = PdfFileReader(path)
        
        #split pdf file to multiple pds
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
            output_filename = 'media/diploma/{}_page_{}.pdf'.format(
                fname, page+1)
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            #print('Created: {}'.format(output_filename))
            
        #convert pdf to png, because tesseracts workd only with png file 
        for page in range(pdf.getNumPages()):
            images = convert_from_path('media/diploma/{}_page_{}.pdf'.format(
                fname, page+1))
            for image in images:
                image.save('media/diploma/{}_page_{}.png'.format(fname, page+1),'PNG')
                image_name2 = 'media/diploma/{}_page_{}.png'.format(fname, page+1)
                #crop name or id
                img = Image.open(image_name2)
                student_id = img.crop((430, 0, 920, 276))
                student_id.save('media/diploma/student_{}.png'.format(page+1))
                img_cv = cv2.imread('media/diploma/student_{}.png'.format(page+1))
                student_id_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
                student_id_text =pytesseract.image_to_string(student_id_rgb)
                if User.objects.filter(last_name=student_id_text).exists():
                    #tesseract converts handwriting to txx file 
                    img_cv = cv2.imread(image_name2)
                    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
                    new =pytesseract.image_to_string(img_rgb)
                    true_answers = open('media/RightAnswers.txt').read()
                    m = SequenceMatcher(None, new, true_answers) #insert mark
                    mark = m.ratio()*1388 #insert markz
                    print(mark)
        return  render(request, 'qmain/check_exam.html', {'title':'Exam check'})
    elif request.method == 'GET':
        return  render(request, 'qmain/check_exam.html', {'title':'Exam check'})

