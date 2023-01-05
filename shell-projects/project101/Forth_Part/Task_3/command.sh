 cat auth.log  | grep  "Failed password for invalid user" | awk {print s/ec2-private_ip/2.2.2.2/g1}| sort | uniq | nl 
