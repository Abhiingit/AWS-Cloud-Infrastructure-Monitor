terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

# Find the latest Amazon Linux 2023 AMI
data "aws_ami" "amazon_linux" {
  most_recent = true

  owners = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }

  filter {
    name   = "state"
    values = ["available"]
  }
}

# EC2 instance
resource "aws_instance" "my_ec2" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  tags = {
    Name        = "cloud-practical-terraform-ec2"
    Environment = "cloud-practical"
  }
}

# S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket_prefix = "cloud-practical-terraform-"

  tags = {
    Name        = "cloud-practical-terraform-bucket"
    Environment = "cloud-practical"
  }
}

# Outputs
output "ec2_instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.my_ec2.id
}

output "s3_bucket_name" {
  description = "S3 bucket name"
  value       = aws_s3_bucket.my_bucket.bucket
}