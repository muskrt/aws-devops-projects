terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~>4"
    }

  }
}

provider "aws" {

  region = "us-east-1"
  profile = "default"
}

data "aws_ami" "AMIID" {
    owners = ["amazon"]
    most_recent = true 
    filter {
      name="name"
      values=["amzn2-ami-hvm*"]
    }
  
}

resource "aws_security_group" "ANSIBLESERVERSECGROUP" {
  ingress{
    from_port = 22
    protocol="tcp"
    to_port=22
    cidr_blocks=["0.0.0.0/0"]
  }
  ingress{
        from_port = 80
    protocol="tcp"
    to_port=80
    cidr_blocks=["0.0.0.0/0"]
  }
  egress{
    from_port = 0
    protocol="-1"
    to_port=0
    cidr_blocks=["0.0.0.0/0"]
  }
  
}

resource "aws_instance" "ANSIBLESERVER" {
  key_name = "linux"
  instance_type = "t2.micro"
  ami = data.aws_ami.AMIID.id  
  vpc_security_group_ids = [aws_security_group.ANSIBLESERVERSECGROUP.id]
  count = 2

  tags = {
    name="worker-node-${count.index}"
  }
    provisioner "local-exec" {
    command="echo worker-node-${count.index} ${self.public_ip}  >> ../ansible/temporary.txt"
  
  }


}

output "ANSIBLESERVER" {
    value = [aws_instance.ANSIBLESERVER[*].tags, aws_instance.ANSIBLESERVER[*].public_ip ]
}

