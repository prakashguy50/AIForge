import unittest
import time
from unittest.mock import patch
from org.mlapi.services.ml_service import MLService


class TestPerformanceWithCloudWatch(unittest.TestCase):

    def setUp(self):
        self.service = MLService()

    @patch("boto3.client")
    def test_cloudwatch_performance_metrics(self, mock_boto3_client):
        # Mock CloudWatch client
        mock_cloudwatch = mock_boto3_client.return_value
        mock_cloudwatch.put_metric_data.return_value = {}

        # Measure performance
        start_time = time.time()
        self.service.perform_some_operation()
        end_time = time.time()
        execution_time = end_time - start_time

        # Log to CloudWatch
        namespace = "MLPlatform/Performance"
        metric_data = [{
            "MetricName": "ExecutionTime",
            "Value": execution_time,
            "Unit": "Seconds"
        }]
        self.service.log_to_cloudwatch(namespace, metric_data)

        # Assertions
        mock_cloudwatch.put_metric_data.assert_called_once()
        self.assertLess(execution_time, 1.0, "Operation took too long!")

if __name__ == "__main__":
    unittest.main()
