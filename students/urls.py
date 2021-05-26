from django.urls import path
from .views import (
    StudentCreateView,
    StudentListView
)

app_name = "students"

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
]