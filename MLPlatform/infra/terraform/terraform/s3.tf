resource aws_s3_bucket mlplatform_bucket {
  bucket = mlplatform-data-bucket
  acl    = private

  versioning {
    enabled = true
  }

  tags = {
    Name        = MLPlatform Data Bucket
    Environment = Production
  }
}
