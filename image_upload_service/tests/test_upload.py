import unittest
from app import app

class ImageUploadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_image_success(self):
        with open('image_upload_service/assets/test_image.jpg', 'rb') as image:
            response = self.app.post('/upload', data={'file': image})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'File uploaded successfully', response.data)

    def test_upload_image_no_file(self):
        response = self.app.post('/upload', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No file part', response.data)

    def test_upload_image_no_selected_file(self):
        response = self.app.post('/upload', data={'file': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No selected file', response.data)

if __name__ == '__main__':
    unittest.main()
