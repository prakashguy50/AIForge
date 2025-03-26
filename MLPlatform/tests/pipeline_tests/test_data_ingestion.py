import unittest
from pipelines.data_ingestion import ingest_data

class TestDataIngestion(unittest.TestCase):
    def test_ingest_data(self):
        # Mock data file path
        file_path = "mock_data.csv"
        data = ingest_data(file_path)
        self.assertIsNotNone(data)
