# bookings/models.py
from django.db import models
from django.contrib.auth.models import User
from travel.models import TravelOption

class Booking(models.Model):
    STATUS_CHOICES = [("Confirmed", "Confirmed"), ("Cancelled", "Cancelled")]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Confirmed")

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.username} for {self.travel_option}"

    @property
    def total_price(self):
        return self.seats_booked * self.travel_option.price
