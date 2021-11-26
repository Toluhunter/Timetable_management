from django import forms
from accounts.models import Department, Courses


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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
        max_length=12,
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
