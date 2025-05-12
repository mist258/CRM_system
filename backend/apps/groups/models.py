from django.db import models


class GroupModel(models.Model):
    class Meta:
        db_table = 'groups'
        ordering = ('id',)

    name = models.CharField(max_length=100, unique=True)
