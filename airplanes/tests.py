from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer

AIRPLANE_URL = "/api/airlines/airplanes/"


class TestUnauthenticated(TestCase):
    def test_create_airplane_authentication_required(self):
        data = {"airplane_id": 2, "passengers_count": 4}
        response = self.client.post(AIRPLANE_URL, data=data)

        self.assertEqual(response.status_code, 401)

    def test_list_airplanes_authentication_required(self):
        response = self.client.get(AIRPLANE_URL)

        self.assertEqual(response.status_code, 401)


class TestAuthenticated(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test",
            password="test",
            first_name="test",
            last_name="test",
        )
        self.client.force_authenticate(user=self.user)
        self.post = Airplane.objects.create(
            airplane_id=2, passengers_count=4, created_by=self.user
        )

    def test_create_airplane_authenticated(self):
        data = {"airplane_id": 2, "passengers_count": 21}
        response = self.client.post(AIRPLANE_URL, data=data)

        self.assertEqual(response.status_code, 201)

    def test_list_airplanes_authenticated(self):
        airplane = Airplane.objects.create(
            airplane_id=20, passengers_count=32, created_by=self.user
        )
        response = self.client.get(AIRPLANE_URL)
        serializer = AirplaneSerializer(airplane)

        self.assertIn(serializer.data,response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_airplane_authenticated(self):
        response = self.client.delete(f"{AIRPLANE_URL}{self.post.id}/")

        self.assertEqual(response.status_code, 204)
