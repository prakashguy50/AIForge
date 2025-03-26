import unittest
from unittest.mock import patch
from org.mlapi.services.ml_service import MLService


class TestDynamoDBIntegration(unittest.TestCase):

    def setUp(self):
        self.service = MLService()

    @patch("boto3.client")
    def test_dynamodb_insert_item(self, mock_boto3_client):
        # Mock DynamoDB client
        mock_dynamodb = mock_boto3_client.return_value
        mock_dynamodb.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

        # Data to insert
        data = {
            "id": {"S": "123"},
            "name": {"S": "Test Item"},
            "timestamp": {"N": "1672531200"}
        }

        # Call service method
        result = self.service.save_to_dynamodb("test_table", data)

        # Assertions
        mock_dynamodb.put_item.assert_called_once_with(
            TableName="test_table",
            Item=data
        )
        self.assertTrue(result)

    @patch("boto3.client")
    def test_dynamodb_query_item(self, mock_boto3_client):
        # Mock DynamoDB client
        mock_dynamodb = mock_boto3_client.return_value
        mock_dynamodb.query.return_value = {
            "Items": [{"id": {"S": "123"}, "name": {"S": "Test Item"}}],
            "Count": 1
        }

        # Query data
        result = self.service.query_dynamodb("test_table", "id", "123")

        # Assertions
        mock_dynamodb.query.assert_called_once()
        self.assertEqual(result["Count"], 1)
        self.assertEqual(result["Items"][0]["name"]["S"], "Test Item")

if __name__ == "__main__":
    unittest.main()
