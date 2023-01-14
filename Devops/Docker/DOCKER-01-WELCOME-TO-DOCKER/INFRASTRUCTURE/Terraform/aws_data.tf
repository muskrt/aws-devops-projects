data "aws_ami" "AMIID" {
    owners = ["amazon"]
    most_recent = true 
    filter{
        name = "virtualization-type"
        values = ["hvm"]
    }
    filter {
        name = "tag:name"
        values = ["amzn-linux-2-*"]
      
    }
  
}