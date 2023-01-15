#!/usr/bin/ruby

requires 'sinatra'
requires 'haml'

get '/' do 
    erb :login 
end

get '/main_page' do 
    haml :main_page
end

get '/error' do 
    erb :error 
end
