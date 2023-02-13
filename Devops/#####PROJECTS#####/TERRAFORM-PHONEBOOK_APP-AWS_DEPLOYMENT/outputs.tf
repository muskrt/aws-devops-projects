data "aws_availability_zones" "available" {
  state = "available"
}

output "list-of-test-vpc" {
  value = data.aws_subnets.subnets.ids
}

output "list_of_az" {
  value = data.aws_availability_zones.available[*].names
}