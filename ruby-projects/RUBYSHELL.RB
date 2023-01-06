#!/bin/ruby

puts "$"
command =gets.chomp 
command_list=`ls /usr/bin` + `ls /usr/sbin`
command_list=command_list.split('\n')
command_list.each{ |item|
    item.upcase!   
}
