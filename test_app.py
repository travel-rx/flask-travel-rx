import app
import json
import os
import unittest

BASE_URL = 'http://localhost:5000/'
ALL_MEDICINES_URL = '{}/user/1/medicines'.format(BASE_URL)

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    # def setUp(self):
    #     self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    #     flaskr.app.testing = True
    #     self.app = flaskr.app.test_client()
    #     with flaskr.app.app_context():
    #         flaskr.init_db()
    #
    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(flaskr.app.config['DATABASE'])

    def test_home_page(self):
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        # import pdb; pdb.set_trace()
        # data = json.loads(response.get_data())
        # self.assertEqual(len(data), 16)

if __name__ == '__main__':
    unittest.main()
