resource "aws_security_group" "alb-sg" {
    name = "albsecuritygroup"
    vpc_id=data.aws_vpc.selected.id
    tags = {
      Name = "Tf+Albsecuritygroup"
    }
    ingress {
        from_port = 80 
        protocol = "tcp"
        to_port = 80
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0 
        protocol ="-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
    } 

resource "aws_security_group" "server-sg" {
    name = "webserversecuritygruop"
    vpc_id=data.aws_vpc.selected.id
    tags = {
      Name = "Tf_webserversecuritygroup"
    }
    ingress {
        from_port = 80 
        protocol = "tcp"
        to_port = 80
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 22 
        protocol = "tcp"
        to_port = 22
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0 
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
     } 

resource "aws_security_group" "db-sg" {
    name = "RDSsecuritygroup"
    vpc_id=data.aws_vpc.selected.id
    tags = {
      Name = "TF_rdsSecurityGroup"
    }
    ingress {
        security_groups = [aws_security_group.server-sg.id]
        from_port = 3306 
        protocol = "tcp"
        to_port = 3306
    }
    egress {
        from_port = 0 
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    } 
    } 

