from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_login(self):
        response = self.client.post(reverse('blog:login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_registration(self):
        response = self.client.post(reverse('blog:register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'pass12345',
            'password2': 'pass12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after registration
        self.assertTrue(User.objects.filter(username='newuser').exists())


# Create your tests here.
