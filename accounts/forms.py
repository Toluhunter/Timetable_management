from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper

User = get_user_model()
class UserCreation(forms.ModelForm):
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password1 =  forms.CharField( label=_("Confirm Password"), widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "department"]
    
    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data["password"]
        password2 = self.cleaned_data["password1"]

        if password1 != password2:
            raise forms.ValidationError("Passwords Must Match")
        
        return super(UserCreation, self).clean(*args, **kwargs)

class StudentCreation(UserCreation):
    is_student = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    choices = [
        ("100", "100 Level"),
        ("200", "200 Level"),
        ("300", "300 Level"),
        ("400", "400 Level"),
    ]
    level = forms.ChoiceField(label=_("Level"), choices=choices)

    class Meta(UserCreation.Meta):
        fields = UserCreation.Meta.fields + ["is_student"]

class LecturerCreation(UserCreation):
    is_lecturer = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta(UserCreation.Meta):
        fields = UserCreation.Meta.fields + ["is_lecturer"]

