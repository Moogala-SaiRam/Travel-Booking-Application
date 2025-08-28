
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from travel.models import TravelOption
from .models import Booking
import datetime

class BookingTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='booker', password='Testpass123')
		self.travel = TravelOption.objects.create(
			type="Bus",
			source="Hyderabad",
			destination="Bengaluru",
			date_time=datetime.datetime.now() + datetime.timedelta(days=1),
			price=500,
			available_seats=10
		)
		self.client.login(username='booker', password='Testpass123')

	def test_booking_creation(self):
		url = reverse('create_booking', args=[self.travel.pk])
		response = self.client.post(url, {'seats': 2})
		self.assertRedirects(response, reverse('booking_list'))
		booking = Booking.objects.get(user=self.user, travel_option=self.travel)
		self.assertEqual(booking.seats_booked, 2)
		self.assertEqual(booking.status, 'Confirmed')
		self.travel.refresh_from_db()
		self.assertEqual(self.travel.available_seats, 8)

	def test_booking_creation_invalid_seats(self):
		url = reverse('create_booking', args=[self.travel.pk])
		response = self.client.post(url, {'seats': 20})
		self.assertContains(response, "Only 10 seats left")
		self.assertFalse(Booking.objects.filter(user=self.user, travel_option=self.travel).exists())

	def test_booking_cancellation(self):
		booking = Booking.objects.create(
			user=self.user,
			travel_option=self.travel,
			seats_booked=3,
			status='Confirmed'
		)
		self.travel.available_seats = 7
		self.travel.save()
		url = reverse('cancel_booking', args=[booking.pk])
		response = self.client.post(url)
		self.assertRedirects(response, reverse('booking_list'))
		booking.refresh_from_db()
		self.assertEqual(booking.status, 'Cancelled')
		self.travel.refresh_from_db()
		self.assertEqual(self.travel.available_seats, 10)
