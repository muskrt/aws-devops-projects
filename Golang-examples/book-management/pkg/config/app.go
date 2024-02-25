package config

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

var (
	db *gorm.DB
)

func Connect() {

	d, err := gorm.Open("mysql", "localhost:3500")
	if err != nil {
		panic(err)

	}
	db = d

}

func GetDb() *gorm.DB {

	return db
}
