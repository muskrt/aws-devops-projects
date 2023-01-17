#!/usr/bin/ruby

require 'sinatra'
require 'haml'

set :bind, '0.0.0.0'
set :port, 3200

get '/main_page' do 
    erb :error
end

get '/main_page/:username' do 
    erb :main_page, { :locals => { :username => params[:username] } }
end

get '/error' do 
    erb :authorize_error 
end
get '/items' do 
    @features = [ 1,2,3,4]
    erb :items, { :locals => { :features => @features } }
end

get '/' do 
    erb :login 
end

post '/' do 
    @name = params["username"]
    @surname = params["password"]
    if @name =="mustafa" and @surname == 'kurt'
        test="/main_page/#{@name}"
        redirect test
    else 
        redirect '/error'
    end
end


