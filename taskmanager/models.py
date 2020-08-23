from django.db import models

# Create your models here.
class Task(models.Model):
    task_no = models.CharField(max_length=32, unique=True)
    task_desc = models.CharField(max_length=32)
