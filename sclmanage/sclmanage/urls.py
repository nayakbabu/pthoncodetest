
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud1/', include('stud1.urls')),
    path('teach1/', include('teacher1.urls'))
]
