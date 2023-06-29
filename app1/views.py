from django.shortcuts import render,redirect
from app1.models import Course
from app1.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')


def add_course(request):
    return render(request,'addcourse.html')

def add_coursedb(request):
    if request.method=="POST":
        course_name=request.POST.get('course')
        course_fee=request.POST.get('fee')
        course=Course( course_name=course_name,fee=course_fee)
        course.save()
        return redirect('/')
    
    
def add_student(request):
    courses=Course.objects.all()
    return render(request,'add_student.html',{'course':courses})


def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        jdate=request.POST['jdate']
        print(jdate)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('/')
    
    
def show_details(request):
    student=Student.objects.all()
    return render(request,'showdetails.html',{'students':student})


def editstudent(request,pk):
    course=Course.objects.all()
    p2=Student.objects.get(id=pk)
    return render(request,'edit.html',{'edit':p2,'course':course})  

 
def edit_student_details(request,pk):  
    if request.method=='POST':
        p2=Student.objects.get(id=pk)
        p2.student_name=request.POST['name']
        p2.student_address=request.POST['addr']
        p2.student_age=request.POST['age']
        p2.joining_date=request.POST['jdate']
        sel=request.POST['sel']
        course=Course.objects.get(id=sel)
        p2.course=course
        p2.save()
        return redirect('show_details')
    return render(request,'edit.html')
 
def deletestudent(request,pk):
    p2=Student.objects.get(id=pk)
    p2.delete()
    return redirect('show_details') 




