from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_create_product', 'Может создавать продукт'),
            ('can_edit_product', 'Может редактировать продукт'),
        ]

    def __str__(self):
        return self.name

