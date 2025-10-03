terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "bedrock" {
  source = "./bedrock"
}

module "lambda" {
  source = "./lambda"
}
