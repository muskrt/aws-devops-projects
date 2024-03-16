package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Server struct {
	db *DB
}

func newserver(database *DB) *Server {
	return &Server{
		db: database,
	}
}

func (s *Server) handleGetRecords(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodGet {
		// results = []bson.M{}
		fmt.Println(s.db.database, s.db.collection)
		results := s.db.Find()
		w.WriteHeader(http.StatusOK)
		w.Header().Add("Content-Type", "application/json")
		json.NewEncoder(w).Encode(results)
	}
	if r.Method == http.MethodPost {
		var data bson.M
		if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
			fmt.Println("line 37", err)
		}
		data, err := s.db.InsertOne(data)
		if err != nil {
			fmt.Println("line 41", err)
		}
		w.WriteHeader(http.StatusOK)
		w.Header().Add("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)

	}

}

func handleErr(err error) {
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
}

type DB struct {
	database   string
	collection string
	client     *mongo.Client
}

func (db *DB) start() (*mongo.Client, error) {
	mongo_url := os.Getenv("MONGO_URL")
	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(mongo_url))
	if err == nil {
		db.client = client
		return client, nil
	} else if err != nil {
		return nil, err
	}
	return nil, nil

}

func (db *DB) Find() []bson.M {
	fmt.Println(db.database, db.collection)
	coll := db.client.Database(db.database).Collection(db.collection)
	query := bson.M{}
	cursor, err := coll.Find(context.TODO(), query)
	handleErr(err)
	results := []bson.M{}
	if err = cursor.All(context.TODO(), &results); err != nil {
		log.Fatal(err)
	}
	return results

}
func (db *DB) InsertOne(data bson.M) (bson.M, error) {

	coll := db.client.Database(db.database).Collection(db.collection)
	_, err := coll.InsertOne(context.TODO(), data)
	if err != nil {
		return nil, err
	}
	return data, err

}

func getDBconnection(database string, collection string) *DB {

	return &DB{
		database:   database,
		collection: collection,
	}
}

func main() {

	db := getDBconnection("todo", "items")
	_, err := db.start()

	handleErr(err)
	server := newserver(db)
	fmt.Println("server started")
	http.HandleFunc("/items", server.handleGetRecords)
	http.ListenAndServe(":3000", nil)

}
