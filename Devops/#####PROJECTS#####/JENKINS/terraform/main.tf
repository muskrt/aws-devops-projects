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
    # owners = ["309956199498"] red hat 
    owners=["amazon"]
    most_recent = true 
    # filter {
    #   name="name"
    #   values=["RHEL-9.0.0_HVM-20230127-x86_64*"]
    # }
    filter {
      name="name"
      values=["amzn2-ami-hvm*"]
    }
  
}
variable "intance_tags" {
    default = ["SLAVE_NODE1","SLAVE_NODE2"]
  
}

resource "aws_security_group" "ANSIBLESERVERSECGROUP" {
  ingress {
    from_port   = 22
    protocol    = "tcp"
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 8080
    protocol    = "tcp"
    to_port     = 8080
    cidr_blocks = ["0.0.0.0/0"]
  }



  egress {
    from_port   = 0
    protocol    = -1
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
  
}
resource "aws_instance" "JENKINS_SERVER" {
  key_name = "linux"
  instance_type = "t2.micro"
  ami = data.aws_ami.AMIID.id  
  root_block_device {
    volume_size = 12
    }
  vpc_security_group_ids = [aws_security_group.ANSIBLESERVERSECGROUP.id]
  count = 1

  tags = {
    Name="JENKINS_SERVER"
  }
    provisioner "local-exec" {
    command=join("",["ansible-pam ${var.build_number} --dyninv ${self.tags.Name} ${self.public_ip} ",
      "${var.inventory_path}/ ec2-user",])

  
  }


}
   

resource "aws_instance" "SLAVE_NODES" {
  key_name = "linux"
  instance_type = "t2.micro"
  ami = data.aws_ami.AMIID.id 
  count=2 
  root_block_device {
    volume_size = 8
    }
  vpc_security_group_ids = [aws_security_group.ANSIBLESERVERSECGROUP.id]

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


