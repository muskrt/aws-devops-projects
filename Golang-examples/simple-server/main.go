package main

import "net/http"

func indexhandler(w http.ResponseWriter, r *http.Request) {

	w.Write([]byte("index page"))
	w.WriteHeader(http.StatusOK)
}

func abouthandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("about page"))

}

func main() {
	println("server starting")
	http.HandleFunc("/", indexhandler)
	http.HandleFunc("/about", abouthandler)
	http.ListenAndServe(":3000", nil)
}
