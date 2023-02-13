data "aws_vpc" "default" {
  default = true
}
data "aws_ami" "MYAMIID" {
    owners = ["amazon"]
    most_recent=true 
    filter{
      name="name"
      values=["amzn2-ami-hvm*"]
    }

    
  
}