#include "crow.h"
#include <string>
#include <iostream>
#include <list>
#include <sstream>
#include <vector>

int main(){

   crow::SimpleApp app; 

    
    CROW_ROUTE(app, "/")([](){
        return "<h1>This Application Created By Mustafa Kurt.</h1>";
    });


    app.port(5000).multithreaded().run();
}