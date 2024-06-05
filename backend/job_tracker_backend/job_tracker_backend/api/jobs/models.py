from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    date_applied = models.CharField(max_length=100)
    compensation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)