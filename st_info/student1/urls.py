from django.urls import path
from . import views
from .views import StudentRecords

urlpatterns = [
    path('school/', StudentRecords.as_view())
]