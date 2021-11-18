from django.shortcuts import render
from django.views import generic
# Create your views here.

class LoginView(generic.TemplateView):
    template_name = 'registration/login.html'

    def post(self, request):
        pass

class SignupView(generic.TemplateView):
    template_name = 'registration/signup.html'

    def post(self, request):
        pass