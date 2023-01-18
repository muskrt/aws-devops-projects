class MainController < ApplicationController
    def index 
        flash.now[:notice] = "logged in successfullly"
    end
end
