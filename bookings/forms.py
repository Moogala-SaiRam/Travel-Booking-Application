# bookings/forms.py
from django import forms

class BookingCreateForm(forms.Form):
    seats = forms.IntegerField(min_value=1, label="Number of seats")

    def __init__(self, *args, **kwargs):
        available = kwargs.pop("available", None)
        super().__init__(*args, **kwargs)
        if available is not None:
            self.fields["seats"].help_text = f"{available} seats available"
