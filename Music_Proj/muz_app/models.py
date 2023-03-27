from django.db import models


class MusicClass(models.Model):
    Song_title = models.CharField(max_length=100, default='')
    Song_Favorite = models.BooleanField(default=False)
    Singer_Name = models.CharField(max_length=100, default='')
    Music_logo = models.IntegerField(max_length=10, default='')
