from django.db import models

class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ("Flight", "Flight"),
        ("Train", "Train"),
        ("Bus", "Bus"),
    ]

    travel_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} | {self.source} → {self.destination} @ {self.date_time}"

    class Meta:
        ordering = ["date_time"]
