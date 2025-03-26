resource "aws_iam_role" "sagemaker_execution_role" {
  name = "MLPlatformSageMakerExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "sagemaker.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_policy_attachment" "sagemaker_policy_attachment" {
  name       = "SageMakerPolicyAttachment"
  roles      = [aws_iam_role.sagemaker_execution_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
}
