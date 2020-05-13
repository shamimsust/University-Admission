from django.db import models


# Create your models here.
class AppliedScienceDepartment(models.Model):
    department_name= models.CharField(max_length=10)
    seat=models.IntegerField()
    class Meta:
        db_table="asdept"
 
class PhysicalScienceDepartment(models.Model):
    department_name= models.CharField(max_length=10)
    seat=models.IntegerField()
    class Meta:
        db_table="psdept"

class SocialScienceDepartment(models.Model):
    department_name= models.CharField(max_length=10)
    seat=models.IntegerField()
class LifeScienceDepartment(models.Model):
    department_name= models.CharField(max_length=10)
    seat=models.IntegerField() 
    class Meta:
        db_table="lsdept"
    
class BBADepartment(models.Model):
    department_name= models.CharField(max_length=10)
    seat=models.IntegerField()  
    class Meta:
        db_table="bbadept"
    
class Student(models.Model):
    photo=models.ImageField(upload_to='student_image',blank=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    fathers_name=models.CharField(max_length=20,default="")
    mothers_name=models.CharField(max_length=20,default="")
    email=models.EmailField(default="", unique=True)
    phone=models.IntegerField(unique=True)
    hsc_gpa=models.FloatField(max_length=5)
    ssc_gpa=models.FloatField(max_length=5)
    group=models.CharField(max_length=10,default="")
    unit=models.CharField(max_length=10,default="")
    department=models.CharField(max_length=10)
    address=models.TextField(max_length=50,default="")
    
    class Meta:
        db_table="student"

