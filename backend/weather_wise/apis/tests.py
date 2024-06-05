from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .models import Temperature, Wind
from rest_framework.test import ApiTestCase

# Create your tests here.
class TempTests(ApiTestCase):
    def setup(self):
        self.temperature = Temperature.objects.create(value=25.0, unit='C')
        self.list_url = reverse('temperature-list')
        self.detail_url = reverse('temperature-detail',kwargs={'pk': self.temp.pk})

    def test_get_all_tempertures(self):

