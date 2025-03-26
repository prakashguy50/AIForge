import unittest
from unittest.mock import patch
from org.mlapi.services.ml_service import MLService


class TestMLServiceAWS(unittest.TestCase):

    def setUp(self):
        self.service = MLService()

    @patch("boto3.client")
    def test_upload_to_s3(self, mock_boto3_client):
        # Mock S3 client
        mock_s3 = mock_boto3_client.return_value
        mock_s3.upload_file.return_value = True

        # Call service method
        result = self.service.upload_to_s3("test_bucket", "test_key", "test_file")

        # Assertions
        mock_s3.upload_file.assert_called_once_with("test_file", "test_bucket", "test_key")
        self.assertTrue(result)

    @patch("boto3.client")
    def test_save_to_dynamodb(self, mock_boto3_client):
        # Mock DynamoDB client
        mock_dynamodb = mock_boto3_client.return_value
        mock_dynamodb.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

        # Call service method
        data = {"id": "1", "prediction": "positive"}
        result = self.service.save_to_dynamodb("test_table", data)

        # Assertions
        mock_dynamodb.put_item.assert_called_once()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
