from django.urls import reverse, resolve
from unittest import TestCase
from .views import fridges, floors, json_view
import unittest


class UrlsTest(TestCase):
    def test_fridges(self):
        url = '/fridges/'
        url2 = reverse(fridges)
        self.assertEquals(url, url2)
        self.assertEquals(resolve(url).func, fridges)
        self.assertEquals(resolve(url2).func, fridges)

    def test_floors(self):
        url = '/floors/'
        url2 = reverse(floors)
        self.assertEquals(url, url2)
        self.assertEquals(resolve(url).func, floors)
        self.assertEquals(resolve(url2).func, floors)
    
    def test_api_json(self):
        url = '/api/json/'
        url2 = reverse(json_view)
        self.assertEquals(url, url2)
        self.assertEquals(resolve(url).func, json_view)
        self.assertEquals(resolve(url2).func, json_view)


if __name__ == '__main__':
    unittest.main()
