
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud/', include('student1.urls')),
    path('teachers/', include('teacherz.urls')),
]
