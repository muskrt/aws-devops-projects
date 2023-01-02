
data "aws_ami" "AMAZONLINUX2"{
    most_recent = true 
    owners = ["amazon"]
    filter{
        name= "virtualization-type"
        values=["hvm"]

    }
    filter {
      name = "name"
      values = ["amzn2-ami-kernel-5.10*"]
    }
}


resource "aws_instance" "myec2" {
    ami = AMIID
    instance_type= INSTANCETYPE
    key_name=KEYNAME
    security_groups = []

    
  
}