"""
Unit tests for the landing page app
"""
import unittest
from flask import url_for
from landing_page.app import create_flask_app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        app = create_flask_app()
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_function(self):
        response = self.client.post('/register', data={'name': 'test name',
                                                       'phone': '1234567890'})  # send a POST request with the form data
        self.assertEqual(response.status_code, 302)  # expect a redirect after successful registration


if __name__ == '__main__':
    unittest.main()
