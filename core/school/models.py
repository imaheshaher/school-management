from django.db import models
from django.contrib.auth.models import AbstractUser
from school.constant_data import USER_TYPE
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=True,null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE,default='student')
class School(models.Model):
     school = models.OneToOneField(User,on_delete=models.CASCADE)
     city = models.CharField(max_length=30,blank=True)
     pincode = models.CharField(max_length=6,blank=True)
class Grade(models.Model):
    grade = models.CharField(max_length=10)

class StudentGrade(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE)