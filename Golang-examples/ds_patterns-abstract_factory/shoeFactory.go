package main

import (
	"strings"
)

type shoe struct {
	shoe_brand string
	price      string
}
type shoe_Factory struct {
	shoes []IProduct
}

func (shoe_product *shoe) getValues() []string {
	values := []string{"shoe_brand: " + shoe_product.shoe_brand, ",price: " + shoe_product.price}
	return values
}

func (a *shoe_Factory) getList() []IProduct {
	// shoes := []IProduct{}
	// for _, value := range a.shoes {

	// 	shoes = append(shoes, IProduct(&value))
	// }

	return a.shoes
}

func (a *shoe_Factory) makeProduct(brand string) IProduct {
	var product shoe
	for _, value := range a.shoes {
		value_brand := string(value.getValues()[0])
		value_price := strings.Split(string(value.getValues()[1]), " ")[1]
		if strings.Contains(value_brand, brand) {
			product = shoe{shoe_brand: brand, price: value_price}
		}
	}
	// return &shoe{}
	return &product
}
