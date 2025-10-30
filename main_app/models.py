from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# ref: cat-collector classwork code
# for auto_now/auto_now add: https://www.geeksforgeeks.org/python/difference-between-autonowadd-and-autonow-in-django/

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='P')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.challenge.title} ({self.get_status_display()})'


MOOD_CHOICES = (
    ('H', 'Happy'),
    ('N', 'Netural'),
    ('S', 'Sad')
)

class Reflection(models.Model):
    user_challenge = models.ForeignKey(UserChallenge, on_delete=models.CASCADE)
    text = models.TextField()
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default='N')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return f"{self.user.username}'s reflection on {self.user_challenge.title} ({self.get_mood_display()})"