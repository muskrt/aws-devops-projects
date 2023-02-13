resource "aws_vpc" "test-vpc" {
  cidr_block = "10.8.0.0/16"
  tags = {
    Name="test-vpc"
  }
  
}

resource "aws_subnet" "public-subnet-1a" {
  vpc_id = aws_vpc.test-vpc.id  
  cidr_block="10.8.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"
  tags = {
    Name = "test-vpc-public"
  }
  
}
resource "aws_subnet" "private-subnet-1a" {
  vpc_id = aws_vpc.test-vpc.id  
  cidr_block="10.8.2.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "test-vpc-private"
  }
  
}
resource "aws_subnet" "public-subnet-1b" {
  vpc_id = aws_vpc.test-vpc.id  
  cidr_block="10.8.4.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1b"
  tags = {
    Name = "test-vpc-public"
  }
  
}
resource "aws_subnet" "private-subnet-1b" {
  vpc_id = aws_vpc.test-vpc.id  
  cidr_block="10.8.5.0/24"
  availability_zone = "us-east-1b"
  tags = {
    Name = "test-vpc-private"
  }
  
}

resource "aws_db_subnet_group" "db-subnet" {
  name="db-subnet-group"
  subnet_ids = ["${aws_subnet.private-subnet-1b.id}","${aws_subnet.private-subnet-1a.id}"]
  
}
resource "aws_internet_gateway" "test-igw" {
  vpc_id = aws_vpc.test-vpc.id  
  tags = {
    Name = "test-igw"
  }
  
}
resource "aws_route_table" "public-rt" {
  vpc_id = aws_vpc.test-vpc.id 
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.test-igw.id
  }
 tags= {
  Name = "test vpc public route table"
 } 
}
resource "aws_route_table_association" "public-1a" {
  subnet_id = aws_subnet.public-subnet-1a.id 
  route_table_id = aws_route_table.public-rt.id
  
}
resource "aws_route_table_association" "public-1b" { 
  subnet_id = aws_subnet.public-subnet-1b.id 
  route_table_id = aws_route_table.public-rt.id
  
}