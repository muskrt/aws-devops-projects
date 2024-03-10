//package classification of Product API
//
//Documentation of Product API
//
//Schemes: http
//BasePath: /
//Version: 1.0.0
//
//Consumes:
// - application/json
//
//Produces:
// - application/json
// swagger:meta

package handlers

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"simple-microservice-2/data"
	"strconv"

	"github.com/gorilla/mux"
)

type Products struct {
	l *log.Logger
}

func NewProducts(l *log.Logger) *Products {
	return &Products{l}

}

func (p *Products) AddProduct(rw http.ResponseWriter, h *http.Request) {
	p.l.Print("handle post request")
	prod := h.Context().Value(KeyProduct{}).(data.Product)
	p.l.Printf("prod : %#v", prod)
	data.AddProduct(&prod)

}
func (p *Products) GetProducts(rw http.ResponseWriter, h *http.Request) {
	lp := data.GetProducts()
	err := lp.ToJSON(rw)
	if err != nil {
		http.Error(rw, "unable to marshal json", http.StatusInternalServerError)
	}
}

func (p *Products) UpdateProducts(rw http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, _ := strconv.Atoi(vars["id"])
	p.l.Print("handle put  request", id)
	prod := r.Context().Value(KeyProduct{}).(data.Product)
	err := data.UpdateProduct(id, &prod)
	if err == data.ErrProductNotFound {
		http.Error(rw, "product not found", http.StatusNotFound)
		return
	}
	if err != nil {
		http.Error(rw, "product not found", http.StatusNotFound)
		return
	}

}

type KeyProduct struct{}

func (p Products) MiddlewareProductValidation(next http.Handler) http.Handler {

	return http.HandlerFunc(func(rw http.ResponseWriter, r *http.Request) {

		prod := data.Product{}
		err := prod.FromJSON(r.Body)
		if err != nil {
			p.l.Println("[ERROR] deserialization of product", err)
			http.Error(rw, "unable to unmarshal json ", http.StatusBadRequest)
			return
		}
		err = prod.Validate()
		if err != nil {
			p.l.Println("[ERROR] validation product", err)
			http.Error(
				rw,
				fmt.Sprintf("Error validating product: %s", err),
				http.StatusBadRequest,
			)
			return

		}

		ctx := context.WithValue(r.Context(), KeyProduct{}, prod)
		r = r.WithContext(ctx)
		next.ServeHTTP(rw, r)
	})
}
