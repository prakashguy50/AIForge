import unittest
from com.org.mlapi.controllers.ml_controller import MLController

class TestMLController(unittest.TestCase):

    def setUp(self):
        # Initialize the controller or any necessary test setup
        self.controller = MLController()

    def test_predict_valid_input(self):
        # Simulate a valid input for prediction
        request_data = {"input": [1.2, 3.4, 5.6]}
        response = self.controller.predict(request_data)
        self.assertEqual(response["status"], "success")
        self.assertIn("prediction", response)

    def test_predict_invalid_input(self):
        # Simulate an invalid input
        request_data = {"invalid_key": [1.2, 3.4]}
        response = self.controller.predict(request_data)
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Invalid input")

if __name__ == "__main__":
    unittest.main()
