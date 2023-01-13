
resource "aws_instance" "MYEC2" {
    key_name = var.key-name
    instance_type= var.instance-type
    count = var.count
    ami= data.aws_ami.AMAZONLINUX.id
    vpc_security_group_ids = [aws_security_group.EC2SECURITYGROUP.id]
  
}


resource "aws_security_group" "EC2SECURITYGROUP" {
  name        = "test"
  description = "Allow SSH AND HTTP inbound traffic"
  vpc_id      = data.aws_vpc.VPCID.id

  ingress {
    description      = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]

  }
   ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
 
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]

  }

  tags = {
    Name = "TFTEST"
  }
  
}

