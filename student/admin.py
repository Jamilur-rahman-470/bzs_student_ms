from django.contrib import admin
from .models import StudentClass, Student
# Register your models here.
class AdminClass(admin.ModelAdmin):
    list_display = ['standard', 'shift', 'section']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'roll']

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentClass, AdminClass)
