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
resource "aws_alb" "name" {
  
}
resource "aws_alb_listener" "name" {
  
}
resource "aws_alb_target_group" "name" {
  
}
resource "aws_alb_target_group_attachment" "name" {
  
}
resource "aws_autoscaling_group" "name" {
  
}