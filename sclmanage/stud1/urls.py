from django.urls import path
from . import views
from .views import StudManage

urlpatterns = [
    path('myscl/', StudManage.as_view())
]