data "aws_ami" "AMIID" {
    owners = ["amazon"]
    most_recent = true 
    filter{
        name = "virtualization-type"
        values = ["hvm"]
    }
    filter {
        name = "name"
        values = ["amzn2-ami-kernel-*"]
      
    }
  
}