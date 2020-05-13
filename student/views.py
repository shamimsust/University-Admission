from django.shortcuts import render, redirect
from student.form import StudentForm
from student.models import Student, AppliedScienceDepartment,\
    PhysicalScienceDepartment, LifeScienceDepartment, SocialScienceDepartment,\
    BBADepartment
from django.contrib.auth.decorators import login_required
from student.utils import render_pdf_view
from django.http.response import HttpResponse
import csv



# Create your views here.
@login_required(login_url='login')
def addstudent(request):
    if request.method == "POST": 
        std = StudentForm(request.POST, request.FILES)  
        if std.is_valid(): 
            try:
                std.save() 
                data = request.POST.copy()
                std_mail=data.get('email')
                return redirect('stdid', email=std_mail)  
            except: 
                pass 
    else:  
        std = StudentForm() 
    print("render")  
    return render(request,'index.html',{'form':std}) 
@login_required(redirect_field_name='login') 
def adddept(request,email,deptname):
    std=Student.objects.get(email=email)
    if std.unit=="as":
        dept=AppliedScienceDepartment.objects.get(department_name=deptname) 
    elif std.unit=="ps":
        dept=PhysicalScienceDepartment.objects.get(department_name=deptname)
    elif std.unit=="ls":
        dept=LifeScienceDepartment.objects.get(department_name=deptname)
    elif std.unit=="ss":
        dept=SocialScienceDepartment.objects.get(department_name=deptname)
    else:
        dept=BBADepartment.objects.get(department_name=deptname)
    count=dept.seat
    count=count-1
    dept.seat=count
    name=dept.department_name
    std.department=name
    dept.save()
    std.save()
    return render(request,'congrats.html',{'std':std})

@login_required(redirect_field_name='login')
def showdept(request,email): 
    std=Student.objects.get(email=email)
    print(std.department)
    if std.unit=="as":
        dept=AppliedScienceDepartment.objects.all() 
        return render(request,"show.html",{'deptlist':dept, 'std':std}) 
    elif std.unit=="ps":
        dept=PhysicalScienceDepartment.objects.all()
        return render(request,"show.html",{'deptlist':dept, 'std':std})
    elif std.unit=="ls":
        dept=LifeScienceDepartment.objects.all()
        return render(request,"show.html",{'deptlist':dept, 'std':std}) 
    elif std.unit=="ss":
        dept=SocialScienceDepartment.objects.all()
        return render(request,"show.html",{'deptlist':dept, 'std':std})
    else:
        dept=BBADepartment.objects.all()
        return render(request,"show.html",{'deptlist':dept, 'std':std}) 
        

def get(request):
    student= Student.objects.all()
    params = {
        'student': student,
        'request': request
    }
    return render_pdf_view('pdf.html', params)
def csv_database_write(request):

    # Get all data from UserDetail Databse Table
    student = Student.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csvoutput.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'email', 'department','image'])

    for std in student:
        writer.writerow([std.first_name, std.last_name, std.email, std.department, std.photo ])

    return response


  
  
  
  
