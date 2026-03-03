provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "apollo" {
  bucket = "apollo-project-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}