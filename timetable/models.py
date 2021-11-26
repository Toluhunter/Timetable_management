from django.db import models
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
    class_start_time = models.TimeField()
    class_end_time = models.TimeField()


class TimeTable(models.Model):
    days = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wenesday', 'Wenesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ]
    levels = [
        ("100", "100 Level"),
        ("200", "200 Level"),
        ("300", "300 Level"),
        ("400", "400 Level"),
    ]
    department = models.ForeignKey(Department, models.SET_NULL, blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, blank=True, null=True)
    day = models.CharField(max_length=10, choices=days)
    level = models.CharField(max_length=3, choices=levels)