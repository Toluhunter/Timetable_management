from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
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

class SelectTimeTableView(IsAdminMixin, generic.FormView):
    template_name = 'createtable.html'
    form_class = SelectTimetableForm

    def form_valid(self, form):
        level = form.cleaned_data["level"]
        department = form.cleaned_data["department"]
        return redirect(reverse('timetable:create', kwargs={"department":department, "level":level}))

class CreateTimeTableView(IsAdminMixin, generic.FormView):
    template_name = "admin.html"
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
            'level':level
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
            'level':self.kwargs["level"]
        })
        return kwargs
    
class TimeTableView(LoginRequiredMixin, generic.TemplateView):
    template_name = "timetable.html"

    def get_context_data(self, **kwargs):
        label = "Level" 
        user = self.request.user
        if user.is_student:
            label = "Lecturer"
            monday = TimeTable.objects.filter(day="monday", department=user.department, level=user.student_set.level)
            tuesday = TimeTable.objects.filter(day="tuesday", department=user.department, level=user.student_set.level)
            wednesday = TimeTable.objects.filter(day="wednesday", department=user.department, level=user.student_set.level)
            thursday = TimeTable.objects.filter(day="thursday", department=user.department, level=user.student_set.level)
            friday = TimeTable.objects.filter(day="friday", department=user.department, level=user.student_set.level)
        else:
            monday = TimeTable.objects.filter(day="monday", department=user.department)
            tuesday = TimeTable.objects.filter(day="tuesday", department=user.department)
            wednesday = TimeTable.objects.filter(day="wednesday", department=user.department)
            thursday = TimeTable.objects.filter(day="thursday", department=user.department)
            friday = TimeTable.objects.filter(day="friday", department=user.department)

        kwargs = super().get_context_data(**kwargs)
        days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday"
        ]
        kwargs.update(
            {
                "days":days,
                "label":label,
                "monday":monday,
                "tuesday":tuesday,
                "wednesday":wednesday,
                "thursday":thursday,
                "friday":friday
            }
        )
        return kwargs