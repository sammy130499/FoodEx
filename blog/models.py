from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(default=10)
    item_logo = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.item_name
