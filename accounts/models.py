import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

# Create your models here.

class CustomManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, department, *args, **kwargs):
        email = self.normalize_email(email)

        department = Department.objects.get(code=department)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            department=department,
            *args,
            **kwargs
        )

        user.set_password(password)
        user.full_clean()
        user.save()
        if user.is_admin:
            lecturer = Lecturer(user=user, initial=f"{user.last_name} .{user.first_name[0].upper()}")
            lecturer.save()
            admin = Admin(lecturer=lecturer)
            admin.save()

        return user
    
    def create_superuser(self, email, first_name, last_name, password, department, *args, **kwargs):
        kwargs.setdefault("is_lecturer", True)
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_admin", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        return self.create_user(email, first_name, last_name, password, department, *args, **kwargs)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_lecturer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'department']
    objects = CustomManager()

    def clean(self, *args, **kwargs):
        email = self.email.strip()
        
        if self.is_student:       
            student_email = re.compile(r"^[a-zA-Z-]{3,}[0-9]{4}@student\.babcock\.edu\.ng$")
            if not student_email.match(email):
                raise ValidationError("Not a Valid babcock email for student")
        elif self.is_lecturer or self.is_admin:
            lecturer_email = re.compile(r"^[a-zA-Z-]{3,}@babcock\.edu\.ng$")
            if not lecturer_email.match(email):
                raise ValidationError("Not a Valid babcock email for staff")

        
        super().clean(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    level = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    initial = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return f'{self.initial}'
    
class Admin(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lecturer.initial}'
class Courses(models.Model):
    department = models.ManyToManyField('Department')
    name = models.CharField(max_length=80)
    level = models.CharField(max_length=3)
    course_code = models.CharField(max_length=10, unique=True, primary_key=True)
    unit = models.CharField(max_length=1)

    def __str__(self):
        return self.course_code

class Department(models.Model):
    name = models.CharField(max_length=60, unique=True)
    code = models.CharField(max_length=10, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=50, unique=True)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.name
