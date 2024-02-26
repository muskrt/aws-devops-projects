package main

type Icar interface {
	setBrand()
	getBrand() string
	setModel()
	getModel() string
	setEngine()
	getEngine() string
	getPrice() string
	getOwnerName() string
}
type car struct {
	brand  string
	model  string
	engine string
	name   string
	price  string
}
type IcarFactory interface {
	makecar(brand string, model string, engine string, name string)
	getMycar(name string) string
}
type carFactory struct {
	car []Icar
}

func getCarfactory() IcarFactory {
	return &carFactory{}

}

func (c *car) setBrand() {
}
func (c *car) getBrand() string {
	return c.brand
}
func (c *car) setModel() {
}
func (c *car) getModel() string {
	return c.model
}
func (c *car) setEngine() {
}
func (c *car) getEngine() string {
	return c.engine
}
func (c *car) getPrice() string {
	return c.price
}
func (c *car) getOwnerName() string {
	return c.name

}
func (factory *carFactory) getMycar(name string) string {
	for _, car := range factory.car {

		if car.getOwnerName() == name {
			return car.getBrand() + " " + car.getModel() + " " + car.getEngine() + " ->price " + car.getPrice() + " dollars"
		}
	}
	return "not found"

}
func (factory *carFactory) makecar(Brand string, Model string, Engine string, Name string) {
	if Brand == "BMW" {
		Car :=
			car{
				brand:  Brand,
				model:  Model,
				engine: Engine,
				name:   Name,
				price:  "350",
			}
		factory.car = append(factory.car, &Car)

	} else if Brand == "Audi" {
		Car :=
			car{
				brand:  Brand,
				model:  Model,
				engine: Engine,
				name:   Name,
				price:  "350",
			}

		factory.car = append(factory.car, &Car)

	}

}
