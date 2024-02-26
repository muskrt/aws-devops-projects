package main

import "fmt"

func main() {

	carfactory := getCarfactory()

	carfactory.makecar("BMW", "1978", "v8", "mustafa")
	fmt.Println(carfactory.getMycar("mustafa"))
}
