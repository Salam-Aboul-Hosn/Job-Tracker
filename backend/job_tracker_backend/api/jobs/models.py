from datetime import timezone
from django.db import models

# Create your models here.
from django.db import models


class Job(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    date_applied = models.CharField(max_length=50, blank=True, null=True) 
    compensation = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
            return self.name