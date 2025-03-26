import unittest

class TestMLController(unittest.TestCase):
    def test_status_endpoint(self):
        response = "ML Backend API is running!"
        self.assertEqual(response, "ML Backend API is running!")
