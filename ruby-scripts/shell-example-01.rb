#!/bin/ruby
require "io/console"
`apt update -y `
`apt upgrade -y `

ARGV.each { |arg|
puts arg 
}
puts ENV['SHELL']
puts ENV['HOME']
puts ENV['$0']

# print "Enter something: "
# x=gets.chomp
# puts "you entered: #{x}"

# password= IO::console.getpass "ENTER PASSWORD: "
# puts "YOUR PASSWORD WAS #{password.length} CHARACTERS LONG."

ARGF.each { |line| 
puts line 
}
open('test1.txt','w') { |output|
output.print "write to it just like std"
output.puts "methods: print , puts ,write"


}

require 'colorize'

puts "blue text ".blue 
puts "bold cyan on blue text".cyan.on_blue.bold 
puts "this #{"fancy".red} text"


puts Dir.pwd 
puts Dir.home 
puts Dir.exists?('try')