package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"strings"

	"github.com/gorilla/mux"
)

type w = http.ResponseWriter
type r = *http.Request

var userDB = map[string]string{
	"mustafa": "passwd",
}

func login(res w, req r) {

	var filename = "login.html"
	T, err := template.ParseFiles(filename)
	if err != nil {
		panic(err)

	}
	err = T.ExecuteTemplate(res, filename, "please log in ")
	if err != nil {
		fmt.Println(err)
	}

}

func loginSubmit(res w, req r) {
	username := req.FormValue("username")
	password := req.FormValue("password")
	vars := mux.Vars(req)
	fmt.Println(vars)
	if userDB[username] == password {
		var filename = "landing.html"
		T, err := template.ParseFiles(filename)
		if err != nil {
			panic(err)
		}
		err = T.ExecuteTemplate(res, filename, nil)
		if err != nil {
			fmt.Println(err)
		}
	} else {
		res.WriteHeader(http.StatusNotFound)
		fmt.Fprint(res, "check your credentials")
	}

}

func handler(res w, req r) {

	switch req.URL.Path {
	case "/login":
		login(res, req)
	case "/login-submit":
		loginSubmit(res, req)
	case "/function":
		filename := "function.html"
		funcMap := map[string]interface{}{
			"upper": strings.ToUpper,
		}
		t, err := template.New(filename).Funcs(funcMap).ParseFiles(filename)
		if err != nil {
			panic(err)
		}
		t.ExecuteTemplate(res, filename, "welcome to the mars")
	default:
		fmt.Fprintf(w(res), "sup men")
	}

}

func main() {
	http.HandleFunc("/", handler)
	port := ":8000"
	method := "http"
	fmt.Printf("server started at %v://localhost%v/login\n", method, port)
	log.Fatal(http.ListenAndServe(port, nil))
	// go run $(go env GOROOT)/src/crypto/tls/generate_cert.go --host=localhost
	// log.Fatal(http.ListenAndServeTLS("", "cert.pem", "key.pem", nil))
}
