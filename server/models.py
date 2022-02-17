from django.db import models

class Todo (models.Model):
    taskname = models.CharField(max_length=30)
 