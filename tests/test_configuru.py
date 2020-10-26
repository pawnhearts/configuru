#!/usr/bin/env python

"""Tests for `configuru` package."""


import unittest
import os

from configuru import Config


class TestConfiguru(unittest.TestCase):
    """Tests for `configuru` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        class MyConfig(Config):
            test: str = 'value'
        self.MyConfig = MyConfig

    def tearDown(self):
        """Tear down test fixtures, if any."""
        if os.path.exists('.env'):
            os.unlink('.env')
        if 'TEST' in os.environ:
            del os.environ['TEST']

    def test_value(self):
        """Test value."""
        self.config = self.MyConfig()
        self.assertEqual(self.config.test, 'value')

    def test_env(self):
        """Test value."""
        os.environ['TEST'] = 'value2'
        self.config = self.MyConfig()
        self.assertEqual(self.config.test, 'value2')

    def test_dotenv(self):
        """Test value."""
        with open('.env', 'w') as f:
            f.write('TEST=value3')
        self.config = self.MyConfig()
        self.assertEqual(self.config.test, 'value3')
