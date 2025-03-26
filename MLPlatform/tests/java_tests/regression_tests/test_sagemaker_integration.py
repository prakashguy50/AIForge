import unittest
from unittest.mock import patch
from org.mlapi.services.ml_service import MLService


class TestSageMakerIntegration(unittest.TestCase):

    def setUp(self):
        self.service = MLService()

    @patch("boto3.client")
    def test_sagemaker_inference(self, mock_boto3_client):
        # Mock SageMaker client
        mock_sagemaker = mock_boto3_client.return_value
        mock_sagemaker.invoke_endpoint.return_value = {
            "Body": b'{"predictions": [0.8]}'
        }

        # Call SageMaker endpoint
        endpoint_name = "test-endpoint"
        input_data = {"instances": [[1.2, 3.4, 5.6]]}
        result = self.service.invoke_sagemaker_endpoint(endpoint_name, input_data)

        # Assertions
        mock_sagemaker.invoke_endpoint.assert_called_once()
        self.assertEqual(result, {"predictions": [0.8]})

if __name__ == "__main__":
    unittest.main()
