from django.urls import path
from .views import (
    StudentSignupView, 
    LecturerSignupView, 
    ActivateAccount, 
    ActivateAccountDone,
    DeleteAccount,
    PasswordChangeView,
)
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordChangeDoneView
)

app_name = 'accounts'
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("delete/", DeleteAccount.as_view(), name='delete'),
    path("signup/student/", StudentSignupView.as_view(), name="studentsignup"),
    path("signup/lecturer/", LecturerSignupView.as_view(), name="lecturersignup"),
    path("activate/<uidb64>/<token>", ActivateAccount.as_view(), name='activate'),
    path("verify/", ActivateAccountDone.as_view(), name='verify'),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(), name="password_change_done")
]