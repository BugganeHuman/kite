from django.db import models
from ordered_model.models import OrderedModel

class Task(OrderedModel):
    task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.TextField()

    class Meta(OrderedModel.Meta):
        pass

class CompletedTask(OrderedModel):
    completed_task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.TextField()
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta(OrderedModel.Meta):
        pass