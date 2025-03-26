resource "aws_sagemaker_model" "ml_model" {
  name                 = "MLPlatformModel"
  execution_role_arn   = aws_iam_role.sagemaker_execution_role.arn
  primary_container {
    image               = "763104351884.dkr.ecr.us-west-2.amazonaws.com/tensorflow-inference:2.7.0-cpu"
    model_data_url      = "s3://mlplatform-data-bucket/models/model.tar.gz"
    environment         = {}
  }
}

resource "aws_sagemaker_endpoint_configuration" "ml_endpoint_config" {
  name = "MLPlatformEndpointConfig"

  production_variants {
    variant_name           = "default"
    model_name             = aws_sagemaker_model.ml_model.name
    initial_instance_count = 1
    instance_type          = "ml.m5.large"
  }
}

resource "aws_sagemaker_endpoint" "ml_endpoint" {
  name                 = "MLPlatformEndpoint"
  endpoint_config_name = aws_sagemaker_endpoint_configuration.ml_endpoint_config.name
}
