import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestFitnessAPI(unittest.TestCase):

    def test_get_classes(self):
        res = requests.get(f"{BASE_URL}/classes")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(isinstance(data, list))

    def test_successful_booking(self):
        payload = {
            "class_id": 1,
            "client_name": "Test User",
            "client_email": "test@example.com"
        }
        res = requests.post(f"{BASE_URL}/book", json=payload)
        self.assertEqual(res.status_code, 201)
        self.assertIn("Booking successful", res.text)

    def test_missing_fields(self):
        res = requests.post(f"{BASE_URL}/book", json={})
        self.assertEqual(res.status_code, 422)

    def test_invalid_email(self):
        payload = {
            "class_id": 1,
            "client_name": "Invalid Email",
            "client_email": "not-an-email"
        }
        res = requests.post(f"{BASE_URL}/book", json=payload)
        self.assertEqual(res.status_code, 422)

    def test_overbooking(self):
        # Try to overbook class_id=2 which has only 3 slots
        for i in range(5):
            payload = {
                "class_id": 2,
                "client_name": f"User{i}",
                "client_email": f"user{i}@test.com"
            }
            res = requests.post(f"{BASE_URL}/book", json=payload)
            if i < 3:
                self.assertEqual(res.status_code, 201)
            else:
                self.assertEqual(res.status_code, 400)
                self.assertIn("No slots available", res.text)


if __name__ == "__main__":
    unittest.main()
