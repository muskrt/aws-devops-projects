data "aws_vpc" "selected" {
    default = true 
  
}
data "aws_subnets" "subnets" {
    filter {
      name = "vpc-id"
      values = [ aws_vpc.test-vpc.id]
    }
  
}
data "aws_ami" "amazon-linux-2" {
    owners = ["amazon"]
    most_recent = true 
    filter{
        name="name"
        values = ["amzn2-ami-hvm*"]
    }

  
}

resource "aws_db_instance" "db-server" {
    instance_class = "db.t2.micro"
    allocated_storage = 10 
    vpc_security_group_ids = [aws_security_group.db-sg.id]
    db_subnet_group_name    = "${aws_db_subnet_group.db-subnet.name}"
    allow_major_version_upgrade = false 
    auto_minor_version_upgrade = true 
    backup_retention_period = 0 
    identifier = "phonebook-app-db"
    db_name = "phonebook"
    engine = "mysql"
    engine_version = "8.0.23"
    username = "admin"
    password = "MUSTAFATOOR"
    monitoring_interval = 0 
    multi_az = false 
    port = 3306 
    publicly_accessible = false 
    skip_final_snapshot = true 

}



resource "local_file" "dbendpoint" {
  content  = aws_db_instance.db-server.address
  filename = "./APP/dbserver.endpoint"

  provisioner "local-exec" {
    command = "cd /home/mustafa/Desktop/aws-devops-projects && git add . && git commit -m 'test' && git push "
    

  
  }
}



resource "aws_launch_template" "asg-lt" {
    name = "phonebook-lt"
    image_id = data.aws_ami.amazon-linux-2.id 
    key_name = "linux" 
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.server-sg.id]
    user_data = filebase64("user-data.sh")
    depends_on = [local_file.dbendpoint]

    tag_specifications {
        resource_type =  "instance"
        tags = {
            Name= "web server of phonebook app"
        }
    }
}

resource "aws_alb_target_group" "app-lb-tg" {
    name = "phonebook-lb-tg"
    port = 80 
    protocol = "HTTP"
    vpc_id = aws_vpc.test-vpc.id
    target_type = "instance"
    health_check {
        healthy_threshold = 2 
        unhealthy_threshold = 3 

    }
  
}

resource "aws_alb" "app-lb" {
    name = "phonebook-lb-tf"
    ip_address_type = "ipv4"
    internal = false 
    load_balancer_type = "application"
    security_groups = [aws_security_group.alb-sg.id]
    subnets = [aws_subnet.public-subnet-1b.id ,aws_subnet.public-subnet-1a.id] 
  
}

resource "aws_alb_listener" "app-listener" {
    load_balancer_arn = aws_alb.app-lb.arn 
    port = 80 
    protocol = "HTTP"
    default_action {
        type="forward"
        target_group_arn = aws_alb_target_group.app-lb-tg.arn 
    }

  
}
resource "aws_autoscaling_group" "app-asg" {
    max_size = 3 
    min_size = 1 
    desired_capacity = 2 
    name = "phonebook-asg"
    health_check_grace_period = 300 
    health_check_type = "ELB"
    target_group_arns = [aws_alb_target_group.app-lb-tg.arn]
    vpc_zone_identifier = aws_alb.app-lb.subnets
    launch_template{
        id = aws_launch_template.asg-lt.id 
        version = aws_launch_template.asg-lt.latest_version
    }
  
}








