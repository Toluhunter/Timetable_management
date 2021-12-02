from django.db import models
from django.core.exceptions import ValidationError


from accounts.models import (
    Courses,
    Lecturer,
    Department,
    Venue
)

# Create your models here.
class Table(models.Model):                                                                                                                                                            
    course_code = models.ForeignKey(Courses, models.CASCADE, db_column='course_code', blank=True, null=True)                                                                       
    lecturer = models.ForeignKey(Lecturer, models.SET_NULL, blank=True, null=True)
    venue_id = models.ForeignKey(Venue, models.SET_NULL, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.course_code} {self.start_time}"

   

class TimeTable(models.Model):
    days = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday')
    ]
    levels = [
        ("100", "100 Level"),
        ("200", "200 Level"),
        ("300", "300 Level"),
        ("400", "400 Level"),
    ]
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=days)
    level = models.CharField(max_length=3, choices=levels)
    
    def __str__(self):
        return f"{self.day} {self.department}"