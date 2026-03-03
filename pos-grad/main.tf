terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
  profile = "cami"
}

resource "aws_s3_bucket" "nexus_production_data" {
  bucket = "nexus-production-data"
  versioning {
    enabled = true
  }
}