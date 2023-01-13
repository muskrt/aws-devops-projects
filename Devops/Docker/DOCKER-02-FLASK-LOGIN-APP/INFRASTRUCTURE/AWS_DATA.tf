data "aws_ami" "AMIID" {

  most_recent      = true
  owners           = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn-linux-2-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
