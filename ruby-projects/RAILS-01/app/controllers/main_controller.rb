class MainController < ApplicationController
    def index 
        flash[:notice] = "logged in successfullly"
    end
end
