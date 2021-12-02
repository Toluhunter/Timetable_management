from django.urls import path
from .views import (
    SelectTimeTableView, 
    EditTimeTableView, 
    TimeTableView,
    TimeTableAdminView
)

app_name = 'timetable'

urlpatterns = [
    path('select/', SelectTimeTableView.as_view(), name="select"),
    path('edit/<department>/<level>/', EditTimeTableView.as_view(), name="edit"),
    path('view/', TimeTableView.as_view(), name="view"),
    path('adminview/<department>/<level>', TimeTableAdminView.as_view(), name="adminview")
]