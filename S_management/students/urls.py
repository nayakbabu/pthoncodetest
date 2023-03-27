from django.urls import path
from . import views


urlpatterns = [
    path('stud/', views.g_data),
    path('class/', views.b_data)
]
