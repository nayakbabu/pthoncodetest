from django.db import models


class Teachers(models.Model):
    Teachername = models.CharField(max_length=10, default='')
    Assigned_Sub = models.CharField(max_length=10, default='')
    Staffroom_no = models.IntegerField(max_length=10, default=8)
