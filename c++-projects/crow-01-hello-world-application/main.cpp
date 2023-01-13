
#include "crow.h"

int main()
{
    crow::SimpleApp app; 

    
    CROW_ROUTE(app, "/")([](){
        return "<h1>This Application Created By Mustafa Kurt.</h1>";
    });

    app.port(5000).multithreaded().run();
}
