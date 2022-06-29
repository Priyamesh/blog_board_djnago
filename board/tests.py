from urllib import response
from django.test import TestCase
from django.urls import reverse_lazy

# Create your tests here.


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse_lazy("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
