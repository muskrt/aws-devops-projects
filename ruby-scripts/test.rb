#!/usr/bin/ruby

require 'colorize'

`ls `
puts `pwd`
DISTRO=`uname -a`.split(" ")
DISTRO.each { |item|
print item + " "
}
puts $?.success?

puts $?.pid

puts $?.exitstatus

puts ENV['HOME']

=begin
ARGF.each { |line| 
puts line 
}
=end

puts "green text ".green
puts "red text".red
puts "yellow test".yellow
puts "cyan".cyan.on_blue.bold
puts "this #{"fancy".red} test"
OUTPUT=`sudo apt-get update`
puts OUTPUT.yellow

