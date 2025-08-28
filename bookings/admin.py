from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("booking_id", "user", "travel_option", "seats_booked", "status", "booking_date")
    list_filter = ("status", "travel_option__type")
    search_fields = ("user__username", "travel_option__source", "travel_option__destination")
