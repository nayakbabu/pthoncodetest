from django.urls import path
from . import views

from .views import Teachers

urlpatterns = [
    path('Teachers/', Teachers.as_view())
]