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
    owners = ["309956199498"]
    most_recent = true 
    filter {
      name="name"
      values=["RHEL-9.0.0_HVM-20230127-x86_64*"]
    }
    # filter {
    #   name="tag:Architecture"
    #   values=["x86_64"]
    # }
  
}
variable "intance_tags" {
    default = ["BACKEND_SERVER","FRONTEND_SERVER","DB_SERVER"]
  
}

resource "aws_security_group" "ANSIBLESERVERSECGROUP" {
  ingress {
    from_port   = 22
    protocol    = "tcp"
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 5000
    protocol    = "tcp"
    to_port     = 5000
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 3000
    protocol    = "tcp"
    to_port     = 3000
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 5432
    protocol    = "tcp"
    to_port     = 5432
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    protocol    = -1
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
  
}

resource "aws_instance" "ANSIBLESERVER" {
  key_name = "linux"
  instance_type = "t2.micro"
  ami = data.aws_ami.AMIID.id  
  vpc_security_group_ids = [aws_security_group.ANSIBLESERVERSECGROUP.id]
  count = 3

  tags = {
    Name="${var.intance_tags[count.index]}"
  }
    provisioner "local-exec" {
    command=join("",["ansible-pam ${var.build_number} --dyninv ${self.tags.Name} ${self.public_ip} ",
      "${var.inventory_path}/ ec2-user",])

  
  }


}
   
   




output "ANSIBLESERVER" {
    value = [aws_instance.ANSIBLESERVER[*].tags, aws_instance.ANSIBLESERVER[*].public_ip ]
}


