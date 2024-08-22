from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender')
        self.receiver = kwargs.pop('receiver')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        tip = super().save(commit=False)
        tip.sender = self.sender
        tip.receiver = self.receiver
        if commit:
            tip.save()
            self.receiver.total_tips_received += tip.amount
            self.receiver.save()
        return tip
