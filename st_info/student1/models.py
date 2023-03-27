from django.db import models


class SchoolModel(models.Model):
    studentname = models.CharField(max_length=10, default='')
    Attendance = models.IntegerField(max_length=10, default=0)
    contact = models.IntegerField(max_length=10, default=0)
