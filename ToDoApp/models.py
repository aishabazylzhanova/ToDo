from django.db import models
from django.contrib.auth.models import User 

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        order_with_respect_to = 'user'
# Create your models here.
