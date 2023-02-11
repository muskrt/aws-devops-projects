data "aws_vpc" "default" {
  default = true
}
data "aws_ami" "MYAMIID" {
    owners = ["amazon"]
    most_recent=true 
    filter{
      key="name"
      values=["amzn2-ami-hvm*"]
    }

    
  
}