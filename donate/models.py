from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Receipt(models.Model):

    PAYMENT_MODE = {
        ('cash','Cash'),
        ('upi','UPI'),
        ('card','Card')
    }

    DEFAULT_MODE = 'cash'

    date = models.DateField()
    name = models.CharField(max_length=70)
    amount = models.PositiveIntegerField()
    mobile = PhoneNumberField(blank=True)
    payment = models.CharField(max_length=4,choices=PAYMENT_MODE, default=DEFAULT_MODE)

    
    def __str__(self) -> str:
        return f"{self.name} ({self.id})"

