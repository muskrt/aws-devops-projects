

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
    ingress{
        from_port=3306
        protocol="tcp"
        to_port=3306
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
    ami =data.aws_ami.MYAMIID.id 
    key_name = var.KEYNAME
    count=var.Num
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.MYSERVER-SEC-GRP.id]
    user_data = file("user-data.sh")
    provisioner "local-exec" {
        command=join("",["ansible-pam ${var.build_number} --dyninv ${self.tags.Name} ${self.public_ip} ",
      "${var.inventory_path}/ ec2-user",])

    }

    connection {
    host = self.public_ip
    type = "ssh"
    user = "ec2-user"
    private_key = file("~/linux.pem")
    }
    provisioner "file" {

    source = "/home/mustafa/Desktop/aws-devops-projects/Devops/PROJECTS/DOCKER-BOOKSTORE_API_APP/App"
    destination = "/home/ec2-user/"

 
    }
}



