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
resource "aws_route_table_association" "test" {
  subnet_id = aws_subnet.public-subnet-1a.id 
  route_table_id = aws_route_table.public-rt.id
  
}