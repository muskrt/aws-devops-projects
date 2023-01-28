
#include <stdlib.h>
#include <iostream>
#include <stdlib.h>
#include <mysql_connection.h>
#include <driver.h>
#include <exception.h>
#include <resultset.h>
#include <statement.h>
#include <crow.h>
using namespace std;
using namespace sql;
int main()
{
    sql::Driver* driver = get_driver_instance();
    // sql::Connection *con;
    // con=driver->connect("tcp://127.0.0.1:3306","root","toor1");

    cout<<"test for db\n";

    return 0;
    // crow::SimpleApp app; 

    
    // CROW_ROUTE(app, "/")([](){
    //     return "<h1>This Application Created By Mustafa Kurt.</h1>";
    // });

    // app.port(5000).multithreaded().run();
}
