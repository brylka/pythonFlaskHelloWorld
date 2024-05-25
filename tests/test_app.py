import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_calc_get(self):
        response = self.app.get('/calc')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form method="post">', response.data)

    def test_calc_post_valid(self):
        response = self.app.post('/calc', data=dict(num1='10', num2='5'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Addition: 15.0', response.data)
        self.assertIn(b'Subtraction: 5.0', response.data)
        self.assertIn(b'Multiplication: 50.0', response.data)
        self.assertIn(b'Division: 2.0', response.data)

    def test_calc_post_division_by_zero(self):
        response = self.app.post('/calc', data=dict(num1='10', num2='0'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Division: Undefined (division by zero)', response.data)

    def test_calc_post_invalid_input(self):
        response = self.app.post('/calc', data=dict(num1='ten', num2='5'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input. Please enter numerical values.', response.data)

if __name__ == '__main__':
    unittest.main()
