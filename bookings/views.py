# bookings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Booking
from .forms import BookingCreateForm
from travel.models import TravelOption

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    return render(request, "bookings/booking_list.html", {"bookings": bookings})

@login_required
def create_booking(request, travel_id):
    travel = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == "POST":
        form = BookingCreateForm(request.POST, available=travel.available_seats)
        if form.is_valid():
            seats = form.cleaned_data["seats"]
            with transaction.atomic():
                t = TravelOption.objects.select_for_update().get(pk=travel.pk)
                if seats > t.available_seats:
                    form.add_error("seats", f"Only {t.available_seats} seats left")
                else:
                    Booking.objects.create(
                        user=request.user,
                        travel_option=t,
                        seats_booked=seats,
                        status="Confirmed",
                    )
                    t.available_seats -= seats
                    t.save(update_fields=["available_seats"])
                    messages.success(request, "Booking confirmed!")
                    return redirect("booking_list")
    else:
        form = BookingCreateForm(initial={"seats": 1}, available=travel.available_seats)

    return render(request, "bookings/booking_form.html", {"travel": travel, "form": form})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking, pk=booking_id, user=request.user, status="Confirmed"
    )
    if request.method == "POST":
        with transaction.atomic():
            t = TravelOption.objects.select_for_update().get(pk=booking.travel_option_id)
            t.available_seats += booking.seats_booked
            t.save(update_fields=["available_seats"])
            booking.status = "Cancelled"
            booking.save(update_fields=["status"])
        messages.info(request, "Booking cancelled.")
        return redirect("booking_list")

    return render(request, "bookings/booking_cancel_confirm.html", {"booking": booking})
