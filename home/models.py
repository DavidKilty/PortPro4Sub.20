

# Tip/models.py

from django.db import models

class Tip(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    def __str__(self):
        return f"Tip of {self.amount} from {self.sender} to {self.receiver} on {self.date}"

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tip_jar_id = models.CharField(max_length=100, unique=True)  # Unique ID for each user's Tip Jar
    bio = models.TextField(blank=True, null=True)  # Optional bio or description for the user
    total_tips_received = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Tip(models.Model):
    sender = models.ForeignKey(User, related_name='sent_tips', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='received_tips', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tip from {self.sender.username} to {self.receiver.user.username} - ${self.amount}"

