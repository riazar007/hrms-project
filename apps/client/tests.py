from django.test import TestCase
from .models import Client  # Assuming there is a Client model in models.py

class ClientModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            name="Test Client",
            email="testclient@example.com",
            phone="1234567890"
        )

    def test_client_creation(self):
        self.assertEqual(self.client.name, "Test Client")
        self.assertEqual(self.client.email, "testclient@example.com")
        self.assertEqual(self.client.phone, "1234567890")

    def test_client_str(self):
        self.assertEqual(str(self.client), "Test Client")  # Assuming __str__ method is defined in Client model

    def test_client_email(self):
        self.assertTrue('@' in self.client.email)  # Simple email validation check

    def test_client_phone_length(self):
        self.assertEqual(len(self.client.phone), 10)  # Assuming phone number should be 10 digits