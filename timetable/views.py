from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .mixins import IsAdminMixin
from django.views import generic
from django.urls import reverse
from .forms import SelectTimetableForm, CreateTimetableForm
from accounts.models import (
    Courses, 
    Department, 
    Lecturer, 
    Admin, 
    Venue
)
from .save_timetable import SaveTimeTable
from .models import TimeTable

# Create your views here.
from django.contrib.auth.views import PasswordResetView

class SelectTimeTableView(IsAdminMixin, generic.FormView):
    template_name = 'select_timetable.html'
    form_class = SelectTimetableForm

    def form_valid(self, form):
        level = form.cleaned_data["level"]
        department = form.cleaned_data["department"]
        action = form.cleaned_data["action"]
        if action == "edit":
            return redirect(reverse('timetable:edit', kwargs={"department":department, "level":level}))
        else:
            return redirect(reverse('timetable:adminview', kwargs={"department":department, "level":level}))


class EditTimeTableView(IsAdminMixin, generic.FormView):
    template_name = "edit_timetable.html"
    form_class = CreateTimetableForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.kwargs["department"]
        level = self.kwargs["level"]
        
        lecturers = Lecturer.objects.filter(user__department__name=department)
        venues = Venue.objects.filter(department__name=department)
        courses = Courses.objects.filter(department__name=department, level=level)

        context.update({
            'lecturers': lecturers, 
            'venues':venues,
            'courses':courses,
            'department':department,
            'level':level,
            
        })

        return context
    
    def form_valid(self, form, *args, **kwargs):
        department = Department.objects.get(name=self.kwargs["department"])
        level = self.kwargs["level"]
        return SaveTimeTable.save(form, department=department, level=level)

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({
            'department':self.kwargs["department"],
            'level':self.kwargs["level"],
            'request':self.request
        })
        if self.request.method == "POST":
            return kwargs
            
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
        types = [ "course", "lecturer", "venue"]
        data={}
        for day in days:
            query = TimeTable.objects.filter(
                level=self.kwargs["level"], 
                department__name=self.kwargs["department"],
                day=day
                )
            if not query.exists():
                continue    
            for timestamp, time in zip(timestamps, times):
                subquery = query.filter(
                    table__start_time=f"{time[0]}:00",
                    table__end_time=f"{time[1]}:00"
                )
                if not subquery.exists():
                    continue
                for value in types:
                    if value == "course":
                        data.update({
                            f"{day}_{value}_{timestamp[0]}_{timestamp[1]}":subquery[0].table.course_code
                        })
                    elif value == "venue":
                        data.update({
                            f"{day}_{value}_{timestamp[0]}_{timestamp[1]}":subquery[0].table.venue_id
                        })
                    elif value == "lecturer":
                        data.update({
                            f"{day}_{value}_{timestamp[0]}_{timestamp[1]}":subquery[0].table.lecturer
                        })

        kwargs.update({"data":data})
        return kwargs

class TimeTableAdminView(IsAdminMixin, generic.TemplateView):
    template_name = 'admin_view.html'

    def get_context_data(self, **kwargs):
        department = self.kwargs["department"]
        level = self.kwargs["level"]

        monday = TimeTable.objects.filter(day="monday", department__name=department, level=level)
        tuesday = TimeTable.objects.filter(day="tuesday", department__name=department, level=level)
        wednesday = TimeTable.objects.filter(day="wednesday", department__name=department, level=level)
        thursday = TimeTable.objects.filter(day="thursday", department__name=department, level=level)
        friday = TimeTable.objects.filter(day="friday", department__name=department, level=level)
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(
                    {
                        "monday":monday,
                        "tuesday":tuesday,
                        "wednesday":wednesday,
                        "thursday":thursday,
                        "friday":friday
                    }
                )
        return kwargs

class TimeTableView(LoginRequiredMixin, generic.TemplateView):
    template_name = "timetable_view.html"

    def get_context_data(self, **kwargs):
        label = "Level" 
        user = self.request.user

        if user.is_student:
            label = "Lecturer"
            monday = TimeTable.objects.filter(day="monday", department=user.department, level=user.student.level)
            tuesday = TimeTable.objects.filter(day="tuesday", department=user.department, level=user.student.level)
            wednesday = TimeTable.objects.filter(day="wednesday", department=user.department, level=user.student.level)
            thursday = TimeTable.objects.filter(day="thursday", department=user.department, level=user.student.level)
            friday = TimeTable.objects.filter(day="friday", department=user.department, level=user.student.level)

        elif user.is_lecturer:
            monday = TimeTable.objects.filter(
                day="monday", 
                department=user.department,
                table__lecturer__initial = user.lecturer.initial
                )
           
            tuesday = TimeTable.objects.filter(
                day="tuesday", 
                department=user.department,
                table__lecturer__initial = user.lecturer.initial
                )
            wednesday = TimeTable.objects.filter(
                day="wednesday", 
                department=user.department,
                table__lecturer__initial = user.lecturer.initial
                )
            thursday = TimeTable.objects.filter(
                day="thursday", 
                department=user.department,
                table__lecturer__initial = user.lecturer.initial
                )
            friday = TimeTable.objects.filter(
                day="friday", 
                department=user.department,
                table__lecturer__initial = user.lecturer.initial
                )

        kwargs = super().get_context_data(**kwargs)
        kwargs.update(
            {
                "label":label,
                "monday":monday,
                "tuesday":tuesday,
                "wednesday":wednesday,
                "thursday":thursday,
                "friday":friday
            }
        )
        return kwargs