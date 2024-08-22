from django.db import models

class Tip(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    def __str__(self):
        return f"Tip of {self.amount} from {self.sender} to {self.receiver} on {self.date}"