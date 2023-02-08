output "server-public-ip" {
    value = aws_instance.MYEC2[*].public_ip
}
output "security-group-id" {
    value = aws_security_group.EC2SECURITYGROUP.arn
}