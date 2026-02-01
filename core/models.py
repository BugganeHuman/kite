from django.db import models
from ordered_model.models import OrderedModel

class Task(models.Model):
    task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.CharField(max_length=50)
    order_field_name = "_order"
    order = models.PositiveIntegerField(editable=False,
                db_index=True, null=True, blank=True)

    class Meta:
        order_with_respect_to = "category"

class CompletedTask(models.Model):
    completed_task = models.TextField()
    owner_id = models.BigIntegerField()
    category = models.CharField(max_length=50)
    completed_at = models.DateTimeField(auto_now_add=True)

