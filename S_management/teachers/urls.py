from django.urls import path
from . import views


urlpatterns = [
    path('sub/', views.teach_sub),
    path('subb/', views.teach_sub2),
]
