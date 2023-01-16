
resource "aws_security_group" "MYSERVER-SECURITY-GROUP" {
    ingress{

    }
    ingress{

    }
    egress{

    }
  
}
resource "aws_instance" "MYSERVER" {
    key_name = var.KEYNAME
    ami = data.aws_ami.AMIID.id
    count = var.NUM
    instance_type = var.INSTANCE-TYPE
    vpc_security_group_ids = [aws_security_group.MYSERVER-SECURITY-GROUP.id]

  
}