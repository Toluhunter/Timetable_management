from django.urls import path
from .views import (
    HomepageView,
    AboutPageView,
    ConatactPageView
)

app_name = "page"

urlpatterns = [
    path('', HomepageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ConatactPageView.as_view(), name="contact")
]