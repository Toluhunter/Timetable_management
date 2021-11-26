from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from .mixins import IsAdminMixin
from django.views import generic
from django.urls import reverse
from .forms import SelectTimetableForm, CreateTimetableForm
from accounts.models import Courses, Lecturer, Admin, Venue
# Create your views here.

class SelectTimeTableView(IsAdminMixin, generic.FormView):
    template_name = 'createtable.html'
    form_class = SelectTimetableForm

    def form_valid(self, form):
        level = form.cleaned_data["level"]
        department_code = form.cleaned_data["department"]
        return redirect(reverse('timetable:create', kwargs={"code":department_code, "level":level}))

class CreateTimeTableView(IsAdminMixin, generic.FormView):
    template_name = "admin.html"
    form_class = CreateTimetableForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.kwargs["code"]
        level = self.kwargs["level"]
        
        lecturers = Lecturer.objects.filter(user__department__name=department)
        admins = Admin.objects.filter(user__department__name=department)
        venues = Venue.objects.filter(department__name=department)
        courses = Courses.objects.filter(department__name=department, level=level)
        print(department)

        context.update({
            'lecturers': lecturers,
            'admins':admins,
            'venues':venues,
            'courses':courses
        })

        return context
