from django import forms
from accounts.models import Department, Courses, Lecturer, Venue
from .models import TimeTable



class SelectTimetableForm(forms.Form):
    choices = [
        ("100", "100 Level"),
        ("200", "200 Level"),
        ("300", "300 Level"),
        ("400", "400 Level"),
    ]
    department = forms.ModelChoiceField(Department.objects.all())
    level = forms.ChoiceField(choices=choices)


class CreateTimetableForm(forms.Form):
    # Monday Courses
    monday_course_7_8 = forms.CharField(
        required=False,
        max_length=12,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_8_9 = forms.CharField(
        required=False,
        max_length=12,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_11_12 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_12_1 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_2_3 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_3_4 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_4_5 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_course_5_6 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Monday Lecturer
    monday_lecturer_7_8 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_8_9 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_9_10 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_10_11 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_11_12 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_12_1 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_2_3 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_3_4 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_4_5 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_lecturer_5_6 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Monday Venue
    monday_venue_7_8 = forms.CharField(
        max_length=12,
        label="Venue",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_8_9 = forms.CharField(
        max_length=12,
        label="Venue",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_10_11 = forms.CharField(
        max_length=12,
        label="Venue",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_11_12 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_12_1 = forms.CharField(
        max_length=12,
        label="Venue",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_2_3 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_3_4 = forms.CharField(
        max_length=12,
        label="Venue",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_4_5 = forms.CharField(
        max_length=12,
        label="Venue",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    monday_venue_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Tuesday Courses
    tuesday_course_7_8 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_11_12 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_12_1 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_2_3 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_4_5 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_course_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Tuesday Lecturer
    tuesday_lecturer_7_8 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_8_9 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_9_10 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_10_11 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_11_12 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_12_1 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_2_3 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_3_4 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_4_5 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_lecturer_5_6 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Tuesday Venue
    tuesday_venue_7_8 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_11_12 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_12_1 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_2_3 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_4_5 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    tuesday_venue_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

 

    # Wednesday Courses
    wednesday_course_7_8 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_11_12 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_12_1 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_2_3 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_4_5 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_course_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Wednesday Lecturer
    wednesday_lecturer_7_8 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_8_9 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_9_10 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_10_11 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_11_12 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_12_1 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_2_3 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_3_4 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_4_5 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_lecturer_5_6 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Wednesday Venue
    wednesday_venue_7_8 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_11_12 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_12_1 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_2_3 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_4_5 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    wednesday_venue_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Thursday Course
    thursday_course_7_8 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_11_12 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_12_1 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_2_3 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_4_5 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_course_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Thursday Lecturer
    thursday_lecturer_7_8 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_8_9 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_9_10 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_10_11 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_11_12 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_12_1 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_2_3 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_3_4 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_4_5 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_lecturer_5_6 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Thursday Venue
    thursday_venue_7_8 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_11_12 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_12_1 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_2_3 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_4_5 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    thursday_venue_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Friday Courses
    friday_course_7_8 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_11_12 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_12_1 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_2_3 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_4_5 = forms.CharField(
        max_length=12,
        label="Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_course_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Course",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Friday Lecturer
    friday_lecturer_7_8 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_8_9 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_9_10 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_10_11 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_11_12 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_12_1 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_2_3 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_3_4 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_4_5 = forms.CharField(
        max_length=25,
        label="Lecturer",
        required=False,
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_lecturer_5_6 = forms.CharField(
        max_length=25,
        required=False,
        label="Lecturer",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    # Friday Venue
    friday_venue_7_8 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_8_9 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_9_10 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_10_11 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_11_12 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_12_1 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_2_3 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_3_4 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_4_5 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )
    friday_venue_5_6 = forms.CharField(
        max_length=12,
        required=False,
        label="Venue",
        widget=forms.TextInput(
            attrs={
                "ondrop": "drop(event)",
                "ondragover": "allowDrop(event)",
                "readonly": True
            }
        )
    )

    def __init__(self, **kwargs):
        self.department = kwargs.pop("department")
        self.level = kwargs.pop("level")

        return super().__init__(**kwargs)


    def clean(self, *args, **kwargs):
        ERROR = forms.ValidationError
        
        for value in self.cleaned_data.values():
            if value:
                break
        else:
            raise forms.ValidationError("Atleast one course must be set on any day")

        department = self.department
        level = self.level
        lecturers = [ 
            f"{lecturer.initial}" 
            for lecturer in Lecturer.objects.filter(user__department__name=department) 
            ]
        venues = [ 
            f"{venue.name}" 
            for venue in Venue.objects.filter(department__name=department) 
            ]
        courses = [ 
            f"{course.course_code}" 
            for course in Courses.objects.filter(department__name=department, level=level) 
            ]
        
        
       
        days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday"
        ]
        timestamps = [
            ('7', '8'),
            ('8', '9'),
            ('9', '10'),
            ('10', '11'),
            ('11', '12'),
            ('12', '1'),
            ('2', '3'),
            ('3', '4'),
            ('4', '5'),
            ('5', '6')
        ]
        for day in days:
            tables = TimeTable.objects.filter(day=day)
            # set_lecturers = TimeTable.objects.filter(day=day)

            for timestamp in timestamps:
                course = f"{day}_course_{timestamp[0]}_{timestamp[1]}"
                venue = f"{day}_venue_{timestamp[0]}_{timestamp[1]}"
                lecturer = f"{day}_lecturer_{timestamp[0]}_{timestamp[1]}"
                try:
                    if self.cleaned_data[course] or\
                        self.cleaned_data[venue] or\
                        self.cleaned_data[lecturer]:

                        if not self.cleaned_data[venue]:
                            self.add_error(venue, ERROR("Cannot be left empty"))
                        else:
                            if not(self.cleaned_data[venue] in venues): 
                                self.add_error(venue, ERROR("Not a Valid venue"))
                            else:
                                try:   
                                    set_venue = tables.get(
                                        table__venue_id__name=self.cleaned_data[venue],
                                        table__start_time=f"{timestamp[0]}:00",
                                        table__end_time=f"{timestamp[1]}:00"
                                    )
                                except TimeTable.DoesNotExist:
                                    set_venue = None
                                finally:
                                    
                                    if set_venue:
                                        print(set_venue.table.venue_id)
                                        self.add_error(venue, ERROR("This Venue is already booked by a different department or level"))

                        if not self.cleaned_data[lecturer]:
                            self.add_error(lecturer, ERROR("Cannot be left empty"))
                        else:
                            if not(self.cleaned_data[lecturer] in lecturers): 
                                self.add_error(lecturer, ERROR("Not a valid Lecturer"))
                            
                            else:
                                try:   
                                    set_lecturer = tables.get(
                                        table__lecturer__initial=self.cleaned_data[lecturer],
                                        table__start_time=f"{timestamp[0]}:00",
                                        table__end_time=f"{timestamp[1]}:00"
                                    )
                                except TimeTable.DoesNotExist:
                                    set_lecturer = None
                                finally:
                                    
                                    if set_lecturer:
                                        self.add_error(lecturer, ERROR("This Lecturer is already booked by a different level"))
                            
                            

                        if not self.cleaned_data[course]:
                            self.add_error(course, ERROR("Cannot be left empty"))
                        else:
                            if not(self.cleaned_data[course] in courses): 
                                self.add_error(course, ERROR("Not a Valid Course"))
                            
                            
                        
                        
                except KeyError:
                    continue

                    

        if self.errors:
            raise forms.ValidationError("Check fields")        
        return super().clean(*args, **kwargs)