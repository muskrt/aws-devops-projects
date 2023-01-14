output "MYSERVER-PUBLIC-IP" {
    value = aws_instance.MYSERVER[*].public_ip
}