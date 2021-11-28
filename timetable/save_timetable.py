from accounts.models import Courses, Lecturer, Venue
from timetable.models import Table, TimeTable
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

class SaveTimeTable:
    def create_table(self, **details):
        for key, value in details.items():
            if not details[key]:
                details[key] = None
            
            elif key == "lecturer":
                details["lecturer"] = Lecturer.objects.get(initial=details["lecturer"])
            
            elif key == "venue_id":
                details["venue_id"] = Venue.objects.get(name=details["venue_id"])

            elif key == "course_code":
                details["course_code"] = Courses.objects.get(course_code=details["course_code"])


        table = Table(
            course_code=details["course_code"],
            lecturer=details["lecturer"],
            venue_id=details["venue_id"],
            start_time=details["start_time"],
            end_time=details["end_time"]
        )
        table.full_clean()
        # table.save()
        return table

    @classmethod
    def save(cls, form:forms.Form, department, level):
        self = SaveTimeTable()
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
        times = [
            ('07', '08'),
            ('08', '09'),
            ('09', '10'),
            ('10', '11'),
            ('11', '12'),
            ('12', '13'),
            ('14', '15'),
            ('15', '16'),
            ('16', '17'),
            ('17', '18')
        ]
        for day in days:
            for timestamp, time in zip(timestamps,times):
                table = self.create_table(
                    course_code=form.cleaned_data[f"{day}_course_{timestamp[0]}_{timestamp[1]}"],
                    lecturer=form.cleaned_data[f"{day}_lecturer_{timestamp[0]}_{timestamp[1]}"],
                    venue_id=form.cleaned_data[f"{day}_venue_{timestamp[0]}_{timestamp[1]}"],
                    start_time=f"{time[0]}:00",
                    end_time=f"{time[1]}:00"
                )

                timetable = TimeTable(
                    department=department, 
                    level=level,
                    table=table,
                    day=f"{day}"
                )
                timetable.full_clean()
                # timetable.save()
        
        return redirect(reverse("page:home"))