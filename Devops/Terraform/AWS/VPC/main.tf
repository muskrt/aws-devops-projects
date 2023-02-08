# resource "local_file" "dbendpoint" {
#   content  = "test"
#   filename = "./dbserver.dbendpoint"
# }

resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.8.0.0/16"
  tags = {
    Name="prod-vpc"
  }
  
}

resource "aws_subnet" "public" {
  vpc_id = aws_vpc.prod-vpc.id  
  cidr_block="10.8.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"
  tags = {
    Name = "prod-vpc-public"
  }
  
}
resource "aws_subnet" "private" {
  vpc_id = aws_vpc.prod-vpc.id  
  cidr_block="10.8.2.0/24"
  tags = {
    Name = "prod-vpc-private"
  }
  
}
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.prod-vpc.id  
  tags = {
    Name = "prod-igw"
  }
  
}
resource "aws_route_table" "public-rt" {
  vpc_id = aws_vpc.prod-vpc.id 
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
 tags= {
  Name = "public route table"
 } 
}
resource "aws_route_table_association" "test" {
  subnet_id = aws_subnet.public.id 
  route_table_id = aws_route_table.public-rt.id
  
}

data "aws_ami" "amazon-linux-2" {
  owners = ["amazon"]
  most_recent = true 
  filter{
    name ="name"
    values=["amzn2-ami-hvm*"]

  }
  
}
resource "aws_security_group" "server-sg" {
  vpc_id = aws_vpc.prod-vpc.id 
  ingress{
    from_port = 22
    protocol = "tcp"
    to_port = 22 
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress{
    from_port = 80
    protocol = "tcp"
    to_port = 80 
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress{
    from_port = 0
    protocol = "-1"
    to_port = 0 
    cidr_blocks = ["0.0.0.0/0"]
  }
  
}

resource "aws_instance" "server-test" {
  ami = data.aws_ami.amazon-linux-2.id 
  key_name = "linux"
  instance_type="t2.micro"
  subnet_id = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.server-sg.id]  


  
}