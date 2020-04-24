from django.urls import reverse, resolve
from unittest import TestCase
from .views import fridges
from . import channels
import unittest


class UrlsTest(TestCase):
    def test_fridges(self):
        url = '/fridges/'
        url2 = reverse(fridges)
        self.assertEquals(url, url2)
        self.assertEquals(resolve(url).func, fridges)
        self.assertEquals(resolve(url2).func, fridges)

class UnitTests(TestCase):
    def test_strings(self):
        self.assertEqual('#general', channels.CHANNEL_NAME_1)


if __name__ == '__main__':
    unittest.main()
