from django.shortcuts import render
from django.utils import timezone
from django.db.models.functions import TruncDate
from .models import TravelOption
import datetime

def travel_list(request):
    travels = TravelOption.objects.filter(date_time__gte=timezone.now()).order_by("date_time")

    # Get filters from query params
    travel_type = request.GET.get("type", "All")
    source = request.GET.get("source", "").strip()
    destination = request.GET.get("destination", "").strip()
    date_str = request.GET.get("date", "")

    # Apply filters
    if travel_type and travel_type != "All":
        travels = travels.filter(type=travel_type)

    if source:
        travels = travels.filter(source__icontains=source)

    if destination:
        travels = travels.filter(destination__icontains=destination)

    if date_str:
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            travels = travels.annotate(date_only=TruncDate("date_time")).filter(date_only=date_obj)
        except ValueError:
            pass  # ignore invalid date

    context = {
        "travels": travels,
        "selected_type": travel_type,
        "source": source,
        "destination": destination,
        "date": date_str,
    }
    return render(request, "travel/travel_list.html", context)
