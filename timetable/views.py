from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from .mixins import IsAdminMixin
from django.views import generic
from django.urls import reverse
from .forms import SelectTimetableForm, CreateTimetableForm
from accounts.models import Courses, Department, Lecturer, Admin, Venue
from .save_timetable import SaveTimeTable
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'department':self.kwargs["department"],
            'level':self.kwargs["level"]
        })
        return kwargs
    
class TimeTableView(generic.TemplateView):
    template_name = "timetable.html"