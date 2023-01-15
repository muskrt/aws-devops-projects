resource "aws_security_group" "MYSERVER-SECURITY-GROUP" {
    ingress{}
    ingress{}
    egress{}
  
}
resource "aws_instance" "MYSERVER" {
    key_name=var.KEYNAME
    instance_type=var.INSTANCE-TYPE
    count=var.NUM
    ami=data.aws_ami.AMIID.id
}