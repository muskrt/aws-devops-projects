package main

type Factory interface {
	getList() []IProduct
	makeProduct(product string) IProduct
}
type IProduct interface {
	getValues() []string
}

func GetFactory(factory string) Factory {
	if factory == "food" {
		return &food_Factory{
			foods: []IProduct{
				&food{food_type: "desert", ingredients: "sugar"}, &food{food_type: "meal", ingredients: "tomate"},
			},
		}
	} else if factory == "Shoe" {
		return &shoe_Factory{
			shoes: []IProduct{
				&shoe{shoe_brand: "adidas", price: "20.5"}, &shoe{shoe_brand: "nike", price: "20.5"},
			},
		}
	}
	return nil
}
