from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    Courses,
    Venue,
    Department,
    Student,
    Lecturer,
    Admin
)
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display = [ "email", "first_name", "last_name", "is_student", "is_lecturer", "is_admin"]
    list_filter = [ "is_admin", "is_lecturer", "is_student"]

admin.site.register(CustomUser, CustomAdmin)
admin.site.register(Courses)
admin.site.register(Venue)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Admin)