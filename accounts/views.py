from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from .models import Student, Lecturer
from .forms import StudentCreation, LecturerCreation
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, Http404

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
# Create your views here.
User = get_user_model()

class LoginView(generic.TemplateView):
    template_name = 'registration/login.html'

    def post(self, request):
        pass

class StudentSignupView(generic.CreateView):
    template_name = 'registration/studentsignup.html'
    form_class = StudentCreation

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        student = Student( user=user, level=form.cleaned_data["level"])
        student.save()

        message = render_to_string('registration/activate_account_email.html',
                {
                    'user': user,
                    'domain': get_current_site(self.request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                }
        )
        email = EmailMessage(
            'Activate Account', 
            message,
            to=[user.email]
        )
        email.send()

        return redirect(self.get_success_url())

    
    def get_success_url(self):
        return reverse("accounts:verify")
        

class LecturerSignupView(generic.CreateView):
    template_name = 'registration/lecturersignup.html'
    form_class = LecturerCreation

    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        lecturer = Lecturer(user=user)
        lecturer.save()
        message = render_to_string('registration/activate_account_email.html',
                {
                    'user': user,
                    'domain': get_current_site(self.request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                }
        )
        email = EmailMessage(
            'Activate Account', 
            message,
            to=[user.email]
        )
        email.send()

        return redirect(self.get_success_url())
 
    def get_success_url(self):
        return reverse("accounts:verify")


class ActivateAccount(generic.TemplateView):
    template_name = 'registration/account_activated.html'

    def get(self, request, *args, **kwargs):
        if not ("token" in self.kwargs and "uidb64" in self.kwargs):
            return HttpResponse('Activation link is invalid!')
        uidb64 = self.kwargs["uidb64"]
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
            token = self.kwargs["token"]
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(self.request, self.template_name)
        else:
            return HttpResponse('Activation link is invalid!')
    

class ActivateAccountDone(generic.TemplateView):
    template_name = 'registration/activation_email_sent.html'

class DeleteAccount(LoginRequiredMixin,generic.TemplateView):
    template_name = 'registration/delete.html'

    def post(self, *args, **kwargs):
        user = self.request.user
        user.delete()
        return redirect(self.get_success_url())

    def get_success_url(self):

        return reverse('page:home')


class PasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("accounts:password_change_done")