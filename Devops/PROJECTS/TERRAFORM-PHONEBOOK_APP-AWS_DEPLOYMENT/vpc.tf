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