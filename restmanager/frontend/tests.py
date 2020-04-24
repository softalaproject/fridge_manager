import unittest
from .views import fridge, fridges
from django.urls import reverse, resolve
from unittest import TestCase
from . import strings


class UrlsTest(TestCase):
    def test_fridges(self):
        url = '/fridges/'
        url2 = reverse(fridges)
        self.assertEquals(url, url2)
        self.assertEquals(resolve(url).func, fridges)
        self.assertEquals(resolve(url2).func, fridges)


class UnitTests(TestCase):
    def test_strings(self):
        self.assertEqual('Saunatilan kaappi on tyhjä.', strings.SLACK_MESSAGE_1)
        self.assertEqual('#general', strings.CHANNEL_NAME_1)
        self.assertEqual('Saunatilan kaappi on täytetty.', strings.SLACK_MESSAGE_2)
        self.assertEqual('Täyttäminen vaiheessa.', strings.SLACK_MESSAGE_3)
        self.assertEqual('Otit vastuun täyttämisestä, viesti laitettu Slackiin.', strings.SUCCESS_MSG_3)


if __name__ == '__main__':
    unittest.main()
