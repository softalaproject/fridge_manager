from .views import fridge, manage, post_beer, post_no_beer
from django.urls import reverse, resolve
from unittest import TestCase
from . import strings

class UrlsTest(TestCase):
    def fridge_test(self):
        url = reverse('')
        self.assertEquals(resolve(url).func, fridge)

    def manage_test(self):
        url = reverse('manage')
        self.assertEquals(resolve(url).func, manage)

    def beer_test(self):
        url = reverse('api/beer')
        self.assertEquals(resolve(url).func, post_beer)

    def no_beer_test(self):
        url = reverse('api/no_beer')
        self.assertEquals(resolve(url).func, post_no_beer)


class UnitTests(TestCase):
    def test_strings(self):
        self.assertEqual('Saunatilan kaappi on tyhjä.', strings.SLACK_MESSAGE_1)
        self.assertEqual('#general', strings.CHANNEL_NAME_1)
        self.assertEqual('Saunatilan kaappi on täytetty.', strings.SLACK_MESSAGE_2)
        self.assertEqual('Täyttäminen vaiheessa.', strings.SLACK_MESSAGE_3)
        self.assertEqual('Otit vastuun täyttämisestä, viesti laitettu Slackiin.', strings.SUCCESS_MSG_3)