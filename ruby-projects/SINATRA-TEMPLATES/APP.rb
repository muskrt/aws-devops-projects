#!/usr/bin/ruby
require 'sinatra'
require 'haml'

set :bind, '0.0.0.0'
set :port, 3200
get '/' do 
    return "this is the main page"
end

get '/contact' do 
    title = params['title']
    author = params['author']
    haml :index, :format => :html5 
end

# get '/', :host_name => /^admin\./ do
#     "Admin Area, Access denied!"
#   end
  
#   get '/', :provides => 'html' do
#     haml :index
#   end
  
#   get '/', :provides => ['rss', 'atom', 'xml'] do
#     builder :feed
#   end