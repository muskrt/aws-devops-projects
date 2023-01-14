
resource "aws_security_group" "MYSERVERSEC-GROUP" {
    ingress {
    description      = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    }
    ingress{
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
        Name = "MYSERVER-SEC-GROUP"
    }
  
}


resource "aws_instance" "MYSERVER" {
    key_name = var.KEYNAME
    instance_type = var.INSTANCE-TYPE
    ami = data.aws_ami.AMIID.id
    count = var.NUM
    vpc_security_group_ids = [aws_security_group.MYSERVERSEC-GROUP.id]
    tags={
        Name="MYTEST-SERVER"
    }
}