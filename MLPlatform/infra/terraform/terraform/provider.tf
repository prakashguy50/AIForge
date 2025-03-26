provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket         = "mlplatform-terraform-state"
    key            = "state/terraform.tfstate"
    region         = var.aws_region
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}
