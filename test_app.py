import unittest
# import json
# import app
BASE_URL = 'http://localhost:5000/'

class TestApp(unittest.TestCase):

    # initial test
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
