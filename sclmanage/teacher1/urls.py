from django.urls import path
from . import views
from .views import TeacherManage

urlpatterns = [
    path('sclteach/', TeacherManage.as_view())
]
