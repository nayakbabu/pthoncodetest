from django.db import models


class SclModel(models.Model):
    Stud_name = models.CharField(max_length=10, default='')
    Stud_result = models.BooleanField(default=False)
    Stud_attend = models.IntegerField(max_length=10, default=0)
    Stud_scl = models.CharField(max_length=100, default='')
