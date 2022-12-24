#!/bin/bash
file=$(cat certificate.pem)
echo -e $file > result.pem
