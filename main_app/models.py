from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# ref: cat-collector classwork code

User = get_user_model()

class Challenge(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title
    

STATUS_CHOICES = (
    ('P', 'Pending'),
    ('IP', 'In progress'),
    ('C', 'Completed')
)

class UserChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pemding')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.challenge.title}'
