from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
from student.models import Student, StudentClass
import csv
import io
from decorators.decorators import allowed_user
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def class_management(request):
    context = {
        'classes': StudentClass.objects.all()
    }
    return render(request, 'custom_admin/class/index.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def delete_all_class(request):
    StudentClass.objects.filter().all().delete()
    return redirect('classes')


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def delete_class(request, **kwargs):
    StudentClass.objects.filter(id=kwargs.get('id')).delete()
    return redirect('classes')


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def search_class(request):
    classes = None
    if request.method == 'POST':
        classes = StudentClass.objects.filter(standard__startswith=request.POST.get('search')).all()
    context = {
        'classes': classes
    }

    return render(request, 'custom_admin/class/index.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def import_classes(request):
    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES['file']
        data = files.read().decode('UTF-8')

        data_stream = io.StringIO(data)
        next(data_stream)
        for col in csv.reader(data_stream, delimiter=',', quotechar="|"):
            StudentClass.objects.create(
                standard=col[0],
                shift=col[1],
                section=col[2]
            )
        return redirect('classes')
    return redirect('classes')


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def add_class(request):

    if request.method == 'POST':
        StudentClass.objects.create(
            standard=request.POST.get('class'),
            section=request.POST.get('section'),
            shift=request.POST.get('shift')
        )

    return redirect('classes')




@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def class_details(request, **kwargs):
    
    context = {
        'class': StudentClass.objects.get(standard= kwargs.get('cls'), section = kwargs.get('sec'))
    }

    return render(request, 'custom_admin/class/detail.html', context)




# STUDENT
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def studen_management(request):
    context = {
        'students': Student.objects.all(),
        'classes': StudentClass.objects.all(),
    }

    return render(request, 'custom_admin/student/index.html', context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def delete_all_student(request):
    Student.objects.filter().all().delete()
    return redirect('students')




@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def import_students(request):
    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES['file']
        data = files.read().decode('UTF-8')

        data_stream = io.StringIO(data)
        next(data_stream)
        for col in csv.reader(data_stream, delimiter=',', quotechar="|"):
            user = User.objects.create(
                username = str(col[2])+str(col[7])+str(col[8]),
                password = str(col[3])+str(col[3])
            )
            groups = Group.objects.get(name ='student')
            groups.user_set.add(user)
            classes = StudentClass.objects.get(standard = col[7], section= col[8])
            student = Student.objects.create(
                owner = user,
                first_name = col[0],
                last_name = col[1],
                roll = col[2],
                phone_no = col[3],
                father_name = col[4],
                mother_name = col[5],
                address = col[6]
            )
            classes.students.add(student)
        return redirect('students')
    return redirect('students')



@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'teacher'])
def add_student(request):
    pass