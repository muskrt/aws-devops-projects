

resource "aws_instance" "myec2" {
    ami = AMIID
    instance_type= INSTANCETYPE
    key_name=KEYNAME
    security_groups = []

    
  
}