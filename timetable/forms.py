from django import forms
from accounts.models import Department

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
    moday = forms.CharField(max_length=12)