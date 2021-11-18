from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class CustomManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, department, *args, **kwargs):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            department=department,
            *args,
            **kwargs
        )

        user.set_password(password)

        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name, password, department, *args, **kwargs):
        kwargs.setdefault("is_student", False)
        kwargs.setdefault("is_staff", True)

        return self.create_user(email, first_name, last_name, password, department, *args, **kwargs)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'department']
    objects = CustomManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    level = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Courses(models.Model):
    department = models.ManyToManyField('Department')
    name = models.CharField(max_length=50, unique=True)
    level = models.CharField(max_length=3)
    course_code = models.CharField(max_length=10, unique=True, primary_key=True)
    unit = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=60, unique=True, primary_key=True)

    def __str__(self):
        return self.name
    
