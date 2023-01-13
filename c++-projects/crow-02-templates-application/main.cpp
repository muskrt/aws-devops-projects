
#include "crow.h"
#include <string>
#include <iostream>
#include <list>
#include <sstream>
#include <vector>

int db_init();
int db_get();
int db_post();
int db_update();
int db_delete();

int main()
{
 
    crow::SimpleApp app; 
    crow::mustache::set_base("./templates");
    crow::mustache::context ctx;

    
    CROW_ROUTE(app, "/")([

    ](){
        
        return crow::mustache::load("index.html").render();
    });


CROW_ROUTE(app,"/test").methods("GET"_method, "POST"_method)
([](const crow::request &req,crow::response &  res){




        if (req.method == "GET"_method )
            return res.redirect_perm("/about");
        
        // else if (req.method == "POST"_method ){

        //     const std::string &location="/";
        //     return res.redirect_perm("/");
        // }

});

CROW_ROUTE(app, "/about").methods("GET"_method, "POST"_method)
(
    [](const crow::request &req){
    

        if (req.method == "GET"_method )
            return crow::mustache::load("about.html").render();

    }
);
CROW_ROUTE(app, "/contact").methods("GET"_method, "POST"_method)
(
    [](const crow::request &req){
    
    if (req.method == "GET"_method ){
    return  crow::response(200,crow::mustache::load("contact.html").render());
    }
    else if (req.method == "POST"_method ){
        return  crow::response(200," redirect test  ");
     
    }
    }
);



    app.port(5000).multithreaded().run();
}
