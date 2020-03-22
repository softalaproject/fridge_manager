import unittest
from . import strings


class StringsTests(unittest.TestCase):
    def test_strings(self):
        self.assertEqual('Saunatilasta on juomat loppu. Haeppa lisää!', strings.SLACKMESSAGE_1)
        self.assertEqual('#general', strings.CHANNEL_NAME_1)
        self.assertEqual('Viesti lähetetty Slack-kanavalle', strings.SUCCESS_MSG_1)
        self.assertEqual('Beer is out', strings.SLACKMESSAGE_2)
        self.assertEqual('#general', strings.CHANNEL_NAME_2)
        self.assertEqual('Message sent', strings.SUCCESS_MSG_2)


if __name__ == '__main__':
    unittest.main()
