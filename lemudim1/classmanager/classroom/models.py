from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
#import misaka

# Create your models here.



class User(AbstractUser): # *
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model): # *
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Student')
    name = models.CharField(max_length=250)
    student_of = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    student_profile_pic = models.ImageField(upload_to="classroom/student_profile_pic", blank=True)

    def get_absolute_url(self):
        return reverse('classroom:student_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['language']


class Teacher(models.Model): # *
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Teacher')
    name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    money_per_hour = models.CharField(max_length=250)
    teacher_profile_pic = models.ImageField(upload_to="classroom/teacher_profile_pic", blank=True)
    class_students = models.ManyToManyField(Student, through="StudentsInClass")
    description = models.TextField()
    payment_way = models.CharField(max_length=250)
    schedule = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('classroom:teacher_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class StudentsInClass(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="class_teacher", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="user_student_name", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ('teacher', 'student')
