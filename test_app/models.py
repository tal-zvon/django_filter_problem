from django.db import models

class NetflowRecord(models.Model):
    timestamp = models.DateTimeField()
