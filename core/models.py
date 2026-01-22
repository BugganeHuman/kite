from django.db import models


class Task(models.Model):
    task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.TextField()

class CompletedTask(models.Model):
    completed_task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.TextField()
    completed_at = models.DateTimeField(auto_now_add=True)