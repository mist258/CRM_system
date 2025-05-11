from django.db import models

from apps.orders.models import OrdersModel
from core.models import BaseModel


class CommentsModel(BaseModel):
    class Meta:
        db_table = 'comments'
        ordering = ('id',)

    text = models.TextField(max_length=100)
    order = models.ForeignKey(OrdersModel, on_delete=models.SET_NULL, null=True, related_name='comments')

