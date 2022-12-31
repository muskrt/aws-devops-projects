#!/usr/bin/ruby

require 'sinatra'

set :bind, '0.0.0.0'
set :port, 3200

get '/' do
	'welcome again sir'

end



