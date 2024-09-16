from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import PermissionsMixin, Group, Permission, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email must be set")
        email = self.normalize_email(email)
        user = self.model(username=email, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
    )


    USERNAME_FIELD = 'email'

    objects = CustomUserManager()


#############################################################################




class StudentManager(CustomUserManager):
    pass


class Student(CustomUser):

    def __str__(self):
        return self.first_name + " " + self.last_name

    USERNAME_FIELD = 'email'


    objects = StudentManager()


class TeacherManager(CustomUserManager):
    pass


class Teacher(CustomUser):

    def __str__(self):
        return self.first_name + " " + self.last_name

    USERNAME_FIELD = 'email'

    objects = TeacherManager()


class PrincipalManager(CustomUserManager):
    pass

class Principal(CustomUser):


    def __str__(self):
        return self.first_name + " " + self.last_name

    USERNAME_FIELD = 'email'

    objects = PrincipalManager()



class Class(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='students')



class Homework(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    file = models.FileField(upload_to='homework', blank=True)
    due_date = models.DateTimeField()
    published = models.BooleanField(default=False)




class Quiz(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    file = models.FileField(upload_to='quizz', blank=True)
    due_date = models.DateTimeField()
    published = models.BooleanField(default=False)



class HomeWorkSubmission(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='homework')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homework_submissions')
    file = models.FileField(upload_to='homework_submissions', blank=True)
    grade = models.FloatField(null=True, blank=True)



class QuizzSubmission(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=False, blank=False)
    quizz = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='quizz')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='quizz_submissions')
    file = models.FileField(upload_to='quizz_submissions', blank=True)
    grade = models.IntegerField(null=True, blank=True)



class Message(models.Model):
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField()
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ManyToManyField(CustomUser, related_name='receiver'),
