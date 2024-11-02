import unittest
from app import app

class NotificationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_notify_success(self):
        response = self.app.post('/notify', json={"message": "Test notification"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Notification sent!', response.data)

    def test_notify_invalid_request(self):
        response = self.app.post('/notify', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid request', response.data)

if __name__ == '__main__':
    unittest.main()
