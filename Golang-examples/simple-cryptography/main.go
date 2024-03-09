package main

import (
	"bufio"
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func encryptMessage(plaintext string) (string, string, string, error) {
	key := string(make([]byte, 32))
	iv := string(make([]byte, 16))
	var plainTextBlock []byte
	// if lengt of the given text is not multiple of iv then complete to multiple iv
	length := len(plaintext)
	if length%16 != 0 {
		extendBlock := 16 - (length % 16)
		fmt.Println(extendBlock)
		plainTextBlock = make([]byte, length+extendBlock)
		copy(plainTextBlock[length:], bytes.Repeat([]byte{uint8(extendBlock)}, extendBlock))
	} else {
		plainTextBlock = make([]byte, length)
	}

	copy(plainTextBlock, plaintext)
	block, err := aes.NewCipher([]byte(key))

	if err != nil {
		return "", "", "", err
	}

	ciphertext := make([]byte, len(plainTextBlock))
	mode := cipher.NewCBCEncrypter(block, []byte(iv))
	mode.CryptBlocks(ciphertext, plainTextBlock)

	str := base64.StdEncoding.EncodeToString(ciphertext)

	return str, key, iv, nil

}

func decryptMessage(encrypted string, key string, iv string) ([]byte, error) {

	ciphertext, err := base64.StdEncoding.DecodeString(encrypted)

	if err != nil {
		return nil, err
	}

	block, err := aes.NewCipher([]byte(key))

	if err != nil {
		return nil, err
	}

	if len(ciphertext)%aes.BlockSize != 0 {
		return nil, fmt.Errorf("block size cant be zero")
	}

	mode := cipher.NewCBCDecrypter(block, []byte(iv))
	mode.CryptBlocks(ciphertext, ciphertext)
	ciphertext = UnPadding(ciphertext)

	return ciphertext, nil
}
func UnPadding(src []byte) []byte {
	length := len(src)
	fmt.Println(length)
	unpadding := int(src[length-1])
	fmt.Println(src[length-1])
	fmt.Println(unpadding)
	fmt.Println(src)
	fmt.Println(src[:(length - unpadding)])
	return src[:(length - unpadding)]
}

func main() {

	fmt.Println("Your message: ")
	data, _ := reader.ReadString('\n')
	// plainText := []byte(data)

	// block, err := aes.NewCipher(token)
	// if err != nil {
	// fmt.Println(err)
	// }

	msg, Key, Iv, _ := encryptMessage(data)
	fmt.Println("Encrypted Message: ", msg)
	dmsg, _ := decryptMessage(msg, Key, Iv)
	fmt.Println("decrypted message: ", string(dmsg))

}
