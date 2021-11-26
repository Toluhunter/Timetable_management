from django.urls import path
from .views import SelectTimeTableView, CreateTimeTableView

app_name = 'timetable'

urlpatterns = [
    path('select/', SelectTimeTableView.as_view(), name="select"),
    path('create/<code>/<level>/', CreateTimeTableView.as_view(), name="create")
]