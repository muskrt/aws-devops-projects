


resource "aws_security_group" "MYSERVERSECURITYGROUP" {
    ingress{


    }
    ingress{

    }
  
}
resource "aws_instance" "MYSERVER" {
    key_name=xxxx
    instance_type = "t2.micro"
    ami = ""
    user_data = file("userdata.sh")
}


