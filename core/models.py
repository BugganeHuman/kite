from django.db import models


class Task(models.Model):
    task = models.TextField()
    owner_id = models.IntegerField()
