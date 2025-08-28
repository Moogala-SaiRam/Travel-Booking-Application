# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_list, name="booking_list"),
    path("create/<int:travel_id>/", views.create_booking, name="create_booking"),
    path("<int:booking_id>/cancel/", views.cancel_booking, name="cancel_booking"),
]
