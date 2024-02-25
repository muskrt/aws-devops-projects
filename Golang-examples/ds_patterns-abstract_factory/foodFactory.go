package main

type food struct {
	food_type   string
	ingredients string
}
type food_Factory struct {
	foods []IProduct
}

func (food_product *food) getValues() []string {
	values := []string{"food_type: " + food_product.food_type, ",ingredients: " + food_product.ingredients}
	return values
}
func (a *food_Factory) getList() []IProduct {
	// foods := []IProduct{}
	// for _, value := range a.foods {
	// 	foods = append(foods, IProduct(&value))
	// }
	return a.foods
}
func (a *food_Factory) makeProduct(product string) IProduct {

	return &food{}
}
