import unittest
import json
import app

class TestApp(unittest.TestCase):

    # initial test
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
