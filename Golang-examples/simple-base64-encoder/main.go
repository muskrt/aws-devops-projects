package main

import (
	"bufio"
	b64 "encoding/base64"
	"fmt"
	"os"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Please provide the data: ")
	data, _ := reader.ReadString('\n')

	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println("Encode operation result: ", sEnc)

	// uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	uDec, _ := b64.URLEncoding.DecodeString(data)
	fmt.Println("Decode operation result: ", string(uDec))
}
