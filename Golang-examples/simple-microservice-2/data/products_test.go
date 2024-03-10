package data

import "testing"

func TestChecksValidation(t *testing.T) {
	p := &Product{
		Name:  "tofas",
		Price: 1.23,
		SKU:   "abc-dfd-adf",
	}
	err := p.Validate()
	if err != nil {
		t.Fatal(err)
	}
}
