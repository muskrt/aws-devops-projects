package main

import (
	"fmt"
	"io"
	"os"
)

func main() {

	fmt.Println("welcome to files in golang")
	content := "this is test message"
	filename := "myLogfile.txt"
	writeToFile(filename, content)
	readfile(filename)

}

func checkNilErr(err error) {
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
}
func writeToFile(filename string, data string) {
	file, err := os.Create(filename)
	checkNilErr(err)
	_, err = io.WriteString(file, data)

	checkNilErr(err)
	defer file.Close()

}
func readfile(filename string) {

	databyte, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	fmt.Printf("the file data is : %s\n", string(databyte))

}
