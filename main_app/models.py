from django.db import models

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return {self.title}


