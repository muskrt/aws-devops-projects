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

resource "aws_instance" "ANSIBLESERVER" {
  key_name = "linux"
  instance_type = "t2.micro"
  ami = data.aws_ami.AMIID.id  
  count = 2

  tags = {
    name="worker-node-${count.index}"
  }
    provisioner "local-exec" {
    command="echo worker-node-${count.index} ${self.public_ip} >> ../ansible/inventory.txt"
  
  }

}

output "ANSIBLESERVER" {
    value = [aws_instance.ANSIBLESERVER[*].tags, aws_instance.ANSIBLESERVER[*].public_ip ]
}

