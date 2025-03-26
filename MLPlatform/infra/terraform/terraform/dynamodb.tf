resource "aws_dynamodb_table" "mlplatform_table" {
  name           = "MLPlatformTable"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Name        = "MLPlatform DynamoDB Table"
    Environment = "Production"
  }
}
