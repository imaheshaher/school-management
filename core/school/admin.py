import imp
from django.contrib import admin
from django.contrib.auth import get_user_model
from school.models import School,StudentGrade,Grade
User = get_user_model()
# Register your models here.
admin.site.register(User)
admin.site.register(School)
admin.site.register(StudentGrade)
admin.site.register(Grade)



