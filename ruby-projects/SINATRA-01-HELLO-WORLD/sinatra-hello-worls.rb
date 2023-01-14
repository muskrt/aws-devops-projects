#!/usr/bin/ruby

require 'sinatra'

set :bind, '0.0.0.0'
set :port, 3200

get '/' do
	'<h1>welcome again sir</h1>'

end



