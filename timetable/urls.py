from django.urls import path
from .views import SelectTimeTableView, CreateTimeTableView, TimeTableView

app_name = 'timetable'

urlpatterns = [
    path('select/', SelectTimeTableView.as_view(), name="select"),
    path('create/<department>/<level>/', CreateTimeTableView.as_view(), name="create"),
    path('timetable/', TimeTableView.as_view(), name="view")
]