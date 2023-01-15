 ## Crow Hello-World Application

 ## Description
 BASIC WEB SERVER APPLICATION FITH CROW 
 FRAMEWORK

 # Table of Contents
 
1. [Title](#Flask-Hello-World-Application)
2. [Description](#Description)
3. [How to Install and Run the Project](#How-to-Install-and-Run-the-Project)
4. [How to Use the Project](#How-to-Use-the-Project) 


 ## How to Install and Run the Project
```CPP
sudo apt-get install -y libasio-dev
sudo apt install cmake -y
git clone https://github.com/CrowCpp/Crow.git
cd Crow
sudo mkdir build
cd build
sudo cmake .. -DCROW_BUILD_EXAMPLES=OFF -DCROW_BUILD_TESTS=OFF
sudo make install
g++ --std=c++11 -o test-app main.cpp -lpthread -static
```

 ## How to Use the Project
 This project can be use to test a port of an host or server