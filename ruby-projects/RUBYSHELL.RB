#!/bin/ruby
loop {
puts "$"
command =gets.chomp 
command.upcase!
if command == "EXIT"
    exit 
else 
    command_list=`ls /usr/bin` + `ls /usr/sbin`
    command_list.upcase!
    COMMAND_ARRAY=command.split(' ')

    COMMAND_ARRAY.each{ |item|
    if (command_list.include? item) &&  (item[0] != '-')
        item.downcase!
    else 

        puts 'cant find '
    end
    }

    NEW_COMMAND=COMMAND_ARRAY.join(" ")
    system(NEW_COMMAND)
end 
}