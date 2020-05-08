import unittest
from unittest import TestCase
from django.urls import reverse, resolve
from .views import fridges, floors, json_view, change_state


class UrlsTest(TestCase):
    """ tests if url matches the function, tests if reversing the function returns the correct url """
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

    def test_api_change_state(self):
        url = '/api/change_state/'
        url2 = reverse(change_state)
        self.assertEquals(url, url2)
        self.assertEquals(resolve(url).func, change_state)
        self.assertEquals(resolve(url2).func, change_state)


if __name__ == '__main__':
    unittest.main()
