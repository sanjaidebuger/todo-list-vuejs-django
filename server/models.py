from django.db import models

class todo (models.Model):
    taskname = models.CharField(max_length=30)
 