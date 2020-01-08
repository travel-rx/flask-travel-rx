import app
from app import db, User, Medicine
import json
import os
import unittest
# import coverage

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
        db.session.close()
        db.drop_all()
        db.create_all()
        #
        # user = User(name='user', email='user@example.com')
        # db.session.add(user)
        # db.session.commit()
        #
        # med1 = Medicine(name='Med 1', generic_name='generic med 1', dosage_amt='1 mg', with_food=1, frequency=3, user_id=user.id)
        # db.session.add(med1)
        # db.session.commit()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_medicines(self):
        user1 = User('user 1', 'user1@example.com')
        db.session.add(user1)
        db.session.commit()

        med2 = Medicine(name='Med 2', generic_name='generic med 2', dosage_amt='2 mg', with_food=1, frequency=3, user_id=user1.id)
        db.session.add(med2)
        db.session.commit()

        med3 = Medicine(name='Med 3', generic_name='generic med 3', dosage_amt='3 mg', with_food=0, frequency=5, user_id=user1.id)
        db.session.add(med3)
        db.session.commit()

        response = self.app.get("/api/v1/user/{}/medicines".format(user1.id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(len(data), 2)

    def test_get_one_medicine(self):
        user3 = User('user 3', 'user1@example.com')
        db.session.add(user3)
        db.session.commit()

        med4 = Medicine(name='Med 4', generic_name='generic med 4', dosage_amt='4 mg', with_food=0, frequency=5, user_id=user3.id)
        db.session.add(med4)
        db.session.commit()

        response = self.app.get("/api/v1/user/{}/medicines/{}".format(user3.id, med4.id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(len(data), 7)

    def test_add_new_medicine(self):
        user4 = User('user 4', 'user1@example.com')
        db.session.add(user4)
        db.session.commit()

        body = {"dosage_amt": "G", "frequency": 5, "generic_name": "OXYCODONE HYDROCHLORIDE AND ACETAMINOPHEN", "name": "Percocet", "user_id": user4.id, "with_food": 0}

        response = self.app.post("/api/v1/user/{}/medicines".format(user4.id), data=json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
