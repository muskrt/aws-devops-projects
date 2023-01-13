

resource "aws_security_group" "MYSERVERSECURITYGROUP" {
    ingress{


    }
    ingress {

        
    }
}


resource "aws_instance" "MYSERVER" {
    key_name=xxxx 
    ami = xxxxx 
    instance_type = "t2.micro"
    vpc_security_group_ids=[MYSERVERSECURITYGROUP.id]

}