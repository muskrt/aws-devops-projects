
resource "aws_instance" "MYEC2" {
    key_name =""
    instance_type= "" 
    count = 1 
    ami= ""
  
}


resource "aws_security_group" "EC2SECURITYGROUP" {
    ingress{

    }
    ingress{
        
    }
  
}