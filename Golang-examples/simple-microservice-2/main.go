package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"simple-microservice-2/handlers"

	"github.com/gorilla/mux"
)

func main() {

	l := log.New(os.Stdout, "product-api", log.LstdFlags)
	PR := handlers.NewProducts(l)

	server := mux.NewRouter()
	getRouter := server.Methods("GET").Subrouter()
	getRouter.HandleFunc("/", PR.GetProducts)

	putRouter := server.Methods("PUT").Subrouter()
	putRouter.HandleFunc("/{id:[0-9]+}", PR.UpdateProducts)
	putRouter.Use(PR.MiddlewareProductValidation)

	postRouter := server.Methods(http.MethodPost).Subrouter()
	postRouter.HandleFunc("/", PR.AddProduct)
	postRouter.Use(PR.MiddlewareProductValidation)

	fmt.Println("server listening on localhost:3000")
	http.ListenAndServe(":3000", server)
}
