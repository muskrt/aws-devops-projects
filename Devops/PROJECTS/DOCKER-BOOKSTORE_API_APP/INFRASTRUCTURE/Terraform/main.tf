

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
    
    provisioner "local-exec" {
        command = "echo http://${self.public_ip} > public_ip.txt"
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
  provisioner "remote-exec" {
    inline = [
        "yum update -y",
        "amazon-linux-extras install docker -y",
        "systemctl start docker",
        "systemctl enable docker",
        "usermod -a -G docker ec2-user",
        "curl -L 'https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose",
        "chmod +x /usr/local/bin/docker-compose",
        "cd /home/ec2-user/App",
        "docker-compose up"
    ]
  }


}

