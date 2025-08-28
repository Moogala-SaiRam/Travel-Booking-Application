
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.register_url = reverse('register')
		self.login_url = reverse('login')
		self.profile_url = reverse('profile')
		self.user_data = {
			'username': 'testuser',
			'password1': 'Testpass123',
			'password2': 'Testpass123',
		}

	def test_user_registration(self):
		response = self.client.post(self.register_url, self.user_data)
		self.assertEqual(response.status_code, 302)  # Redirect after registration
		self.assertTrue(User.objects.filter(username='testuser').exists())

	def test_user_login(self):
		User.objects.create_user(username='testuser', password='Testpass123')
		response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'Testpass123'})
		self.assertEqual(response.status_code, 302)  # Redirect after login

	def test_profile_access_requires_login(self):
		response = self.client.get(self.profile_url)
		self.assertEqual(response.status_code, 302)  # Redirect to login
