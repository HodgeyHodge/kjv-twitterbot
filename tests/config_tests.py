import unittest
import sys
import os
import tweepy

from Twitterbot.src import config


class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        self.config = config.Config()

    def test_config_exists(self):
        self.assertIsInstance(self.config.api_context, tweepy.API)
        self.assertIsInstance(self.config.fonts, list)
        self.assertIsInstance(self.config.icons, list)
        self.assertIsInstance(self.config.light, int)
        self.assertIsInstance(self.config.dark, int)

    def test_config_fonts_exist(self):
        for font in self.config.fonts:
            font_path = os.path.join('Twitterbot/assets/fonts/', font)
            self.assertTrue(os.path.exists(font_path))

    def test_config_icons_exist(self):
        for icon in self.config.icons:
            icon_path = os.path.join('Twitterbot/assets/icons/', icon.Filename)
            self.assertTrue(os.path.exists(icon_path))


if __name__ == '__main__':
    unittest.main()