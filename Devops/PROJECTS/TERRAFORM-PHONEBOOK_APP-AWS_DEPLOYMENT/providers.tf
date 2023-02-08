terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.53.0"
    }

    github = {
      source = "integrations/github"
      version = "5.17.0"
    }
  }
}

provider "aws" {

  region = "us-east-1"
  profile = default
}




provider "github" {
  token = ""
}