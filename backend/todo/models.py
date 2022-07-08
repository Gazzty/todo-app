from typing_extensions import Required
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=25, blank = False)
    description = models.CharField(max_length=100)
    end_date = models.DateField(blank = False)