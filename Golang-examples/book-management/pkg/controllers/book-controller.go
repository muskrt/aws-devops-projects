package controllers

import (
	"book-management/pkg/models"
	"book-management/pkg/utils"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

var Newbook models.Book

func GetBook(w http.ResponseWriter, r *http.Request) {
	newBooks := models.GetAllBook()
	res, _ := json.Marshal(newBooks)
	w.Header().Set("content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(res)

}
func GetBookById(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	bookId := vars["bookId"]
	ID, err := strconv.ParseInt(bookId, 0, 0)
	if err != nil {
		fmt.Println("error while parsing ")
	}
	bookDetails, _ := models.GetBookById(ID)
	res, _ := json.Marshal(bookDetails)
	w.Header().Set("content-type", "applicatoin/json")
	w.WriteHeader(http.StatusOK)
	w.Write(res)

}
func CreateBook(w http.ResponseWriter, r *http.Request) {
	Createbook := &models.Book{}
	utils.ParseBody(r, Createbook)
	b := Createbook.CreateBook()
	res, _ := json.Marshal(b)
	w.WriteHeader(http.StatusOK)
	w.Write(res)

}
func DeleteBook(w http.ResponseWriter, r *http.Request) {

	vars := mux.Vars(r)
	bookId := vars["bookId"]
	ID, err := strconv.ParseInt(bookId, 0, 0)
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	book := models.DeleteBook(ID)
	res, _ := json.Marshal(book)
	w.Header().Set("content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(res)

}
func UpdateBook(w http.ResponseWriter, r *http.Request) {

	var updatebook = &models.Book{}

	utils.ParseBody(r, updatebook)
	vars := mux.Vars(r)
	bookId := vars["bookId"]
	ID, err := strconv.ParseInt(bookId, 0, 0)
	if err != nil {

		fmt.Println("error while parsing")
		panic(err)
	}

	booksdetails, db := models.GetBookById(ID)
	if updatebook.Name != "" {
		booksdetails.Name = updatebook.Name

	}

	if updatebook.Author != "" {
		booksdetails.Author = updatebook.Author
	}
	if updatebook.Publication != "" {
		booksdetails.Publication = updatebook.Publication
	}
	db.Save(&booksdetails)
	res, _ := json.Marshal(booksdetails)
	w.Header().Set("content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(res)

}
