

resource "aws_security_group" "MYSERVER-SEC-GRP" {
    ingress{}
    ingress{}
    egress{}
  
}

resource "aws_instance" "MYSERVER" {
    ami = ""
    key_name = var.KEYNAME
    count=var.Num
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.MYSERVER-SEC-GRP.id]
  
}