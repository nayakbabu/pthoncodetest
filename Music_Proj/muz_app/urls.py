from django.urls import path
from.import views
from.views import MusicData

urlpatterns = [
    path('muapp/', MusicData.as_view())

]