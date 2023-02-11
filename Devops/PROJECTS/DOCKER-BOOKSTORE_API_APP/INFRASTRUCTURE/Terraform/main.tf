

resource "aws_security_group" "MYSERVER-SEC-GRP" {
    ingress{
        from_port=80
        protocol="tcp"
        to_port=80
        cidr_blocks=["0.0.0.0/0"]
    }
    ingress{
        from_port=22
        protocol="tcp"
        to_port=22
        cidr_blocks=["0.0.0.0/0"]

    }
    egress{
        from_port=0
        protocol="-1"
        to_port=0
        cidr_blocks=["0.0.0.0/0"]
    }
  
}

resource "aws_instance" "MYSERVER" {
    ami ="" 
    key_name = var.KEYNAME
    count=var.Num
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.MYSERVER-SEC-GRP.id]
  
}

