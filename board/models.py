from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
