from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import PermissionsMixin, Group, Permission, AbstractBaseUser, User
from django.db import models
from django.conf import settings
#############################################################################

class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures")


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures")


class PrincipalProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures")

#####################################################################################



class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='classes')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='student_class')
    timetable = models.JSONField(default=dict)


    def __str__(self):
        return self.name



class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='Assignment/assignment', blank=True)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    dateline = models.DateTimeField()

    def __str__(self):
        return self.title





class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Assignment/submission', blank=True)
    content = models.TextField(blank=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True, null=True)





class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='Quiz/quiz')
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    dateline = models.DateTimeField()

    def __str__(self):
        return self.title



class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    file = models.FileField(upload_to='Quiz/submission')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.IntegerField()




class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='msg_sent')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='msg_received')
    to_class = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True, related_name='all_msg')
    to_parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='parent_msg')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.content[20]
