from django.shortcuts import render,redirect
 
# Create your views here.
from .models import StudentInfo
 
 
def home(request): # READ
 
    all_students = StudentInfo.objects.all()
 
    context ={
        'all_students':all_students,
         
        }
    return render(request,'index.html',context)
 
 
def add_student(request): # CREATE
 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
 
        #print(10*'---',name,email,phone)
 
        student = StudentInfo(name=name,email=email,phone=phone)
        student.save()
        return redirect('home')
 
 
    return render(request,'index.html')
 
 
def delete_student(request,id): #DELETE
 
    student = StudentInfo.objects.get(id=id)
    student.delete()
    return redirect('home')
 
    #return render(request,'index.html')
 
 
def edit_student(request,id): #UPDATE
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
 
        #print(10*'---',name,email,phone)
 
        student = StudentInfo.objects.get(id=id)
 
        student.name = name
        student.email = email
        student.phone = phone
        student.save()
         
        return redirect('home')
 
    else:
        student = StudentInfo.objects.get(id=id)
        context = {
            'student':student,
        }
        return render(request,'edit.html',context)
