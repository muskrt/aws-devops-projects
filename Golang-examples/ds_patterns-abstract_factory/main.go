package main

import "fmt"

func main() {

	shoefactory := GetFactory("Shoe")
	productlist := shoefactory.getList()
	for i := 0; i < len(productlist); i++ {
		food := productlist[i]
		fmt.Println(food.getValues())
	}
	shoe := shoefactory.makeProduct("adidas")
	fmt.Println("Your product is ready: ", shoe.getValues())
	foodfactory := GetFactory("food")
	productlist = foodfactory.getList()

	for i := 0; i < len(productlist); i++ {
		food := productlist[i]
		fmt.Println(food.getValues())
	}

}
