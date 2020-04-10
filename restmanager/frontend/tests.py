import unittest
from . import strings


class StringsTests(unittest.TestCase):
    def test_strings(self):
        self.assertEqual('Saunatilan kaappi on tyhjä.', strings.SLACK_MESSAGE_1)
        self.assertEqual('#general', strings.CHANNEL_NAME_1)
        self.assertEqual('Saunatilan kaappi on täytetty.', strings.SLACK_MESSAGE_2)
        self.assertEqual('Täyttäminen vaiheessa.', strings.SLACK_MESSAGE_3)
        self.assertEqual('Otit vastuun täyttämisestä, viesti laitettu Slackiin.', strings.SUCCESS_MSG_3)


if __name__ == '__main__':
    unittest.main()
