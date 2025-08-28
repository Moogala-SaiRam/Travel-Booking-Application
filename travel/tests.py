
from django.test import TestCase, Client
from django.urls import reverse
from .models import TravelOption
import datetime

class TravelOptionTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.travel1 = TravelOption.objects.create(
			type="Bus",
			source="Hyderabad",
			destination="Bengaluru",
			date_time=datetime.datetime.now() + datetime.timedelta(days=1),
			price=500,
			available_seats=40
		)
		self.travel2 = TravelOption.objects.create(
			type="Flight",
			source="Hyderabad",
			destination="Mumbai",
			date_time=datetime.datetime.now() + datetime.timedelta(days=2),
			price=3000,
			available_seats=10
		)
		self.url = reverse('travel_list')

	def test_travel_list_view(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Hyderabad")
		self.assertContains(response, "Bengaluru")
		self.assertContains(response, "Mumbai")

	def test_travel_filter_by_type(self):
		response = self.client.get(self.url, {'type': 'Flight'})
		self.assertContains(response, "Flight")
		# Only check for 'Bus' in table rows, not in dropdown
		self.assertNotIn(b'<td>Bus</td>', response.content)

	def test_travel_filter_by_destination(self):
		response = self.client.get(self.url, {'destination': 'Bengaluru'})
		self.assertContains(response, "Bengaluru")
		self.assertNotContains(response, "Mumbai")
