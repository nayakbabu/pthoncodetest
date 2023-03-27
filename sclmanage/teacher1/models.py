from django.db import models


class TeachModel(models.Model):
    Teach_name = models.CharField(max_length=10, default='')
    Teach_room = models.IntegerField(max_length=10, default=0)
    Teach_sub = models.CharField(max_length=10, default='')

