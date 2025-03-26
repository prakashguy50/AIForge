import unittest
from com.yourcompany.mlapi.controllers.ml_controller import MLController

class TestMLRegression(unittest.TestCase):

    def setUp(self):
        self.controller = MLController()

    def test_regression_case_1(self):
        # Example: Test a specific input-output combination
        request_data = {"input": [0.5, 1.5, 2.5]}
        response = self.controller.predict(request_data)
        expected_prediction = {"status": "success", "prediction": [0.1, 0.3, 0.5]}
        self.assertEqual(response, expected_prediction)

if __name__ == "__main__":
    unittest.main()
