from django.db import models

# Create your models here.
class StudentClass(models.Model):
    
    standard = models.IntegerField()
    shift = models.CharField(max_length=10)
    section = models.CharField(max_length=2)
    students = models.ManyToManyField(to='Student')
    #techer = models.OneToOneField(to='Teacher')

    def __str__(self):
        return str(self.standard) + '  ' + self.section


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    phone_no = models.IntegerField()
    
    father_name = models.CharField(max_length=70)
    mother_name = models.CharField(max_length=70)
    father_phone = models.IntegerField()
    address = models.TextField()

    def __str__(Self):
        return Self.first_name + '  ' + Self.last_name

