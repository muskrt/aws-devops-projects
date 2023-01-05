
resource "aws_instance" "MYEC2" {
    key_name =""
    instance_type= "" 
    count = 1 
    ami= ""
  
}


resource "aws_security_group" "EC2SECURITYGROUP" {
  name        = "test"
  description = "Allow TLS inbound traffic"
  vpc_id      = data.aws_vpc.VPCID

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
    Name = "allow_tls"
  }
  
}