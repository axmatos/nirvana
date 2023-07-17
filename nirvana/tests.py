import json

from django.test import TestCase
from django.urls import reverse

from nirvana import views


class ApiViewTests(TestCase):
    def test_api1(self):
        response = self.client.get(reverse('api1'))
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content)
        self.assertEqual(json_content, views.get_json_dict(1000, 10000, 5000))

    def test_api2(self):
        response = self.client.get(reverse('api2'))
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content)
        self.assertEqual(json_content, views.get_json_dict(1200, 13000, 6000))

    def test_api3(self):
        response = self.client.get(reverse('api3'))
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content)
        self.assertEqual(json_content, views.get_json_dict(1000, 10000, 6000))

    def test_api_average(self):
        response = self.client.get(reverse('api'))
        self.assertEqual(response.status_code, 200)
        json_content = json.loads(response.content)
        self.assertEqual(json_content, views.get_json_dict(1066, 11000, 5666))
