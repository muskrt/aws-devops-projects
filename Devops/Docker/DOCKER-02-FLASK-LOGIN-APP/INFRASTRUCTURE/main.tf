

resource "aws_instance" "MYEC2"{
    key_name = xxxx 
    ami = data.aws_ami.AMIID
    instance_type = "t2.micro"
    count=1
    user_data = file("userdata.sh")

    



}