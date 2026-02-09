from django.db import models
from positions import PositionField


class Task(models.Model):
    task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.CharField(max_length=50)
    position = PositionField(collection='category')

    class Meta:
        ordering = ['position']

class CompletedTask(models.Model):
    completed_task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.CharField(max_length=50)
    completed_at = models.DateTimeField(auto_now_add=True)

