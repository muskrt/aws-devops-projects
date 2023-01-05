data "aws_vpc" "VPCID" {
    default = true
  
}

data "aws_ami" "AMAZONLINUX" {
    most_recent = true
    owners = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

 
}