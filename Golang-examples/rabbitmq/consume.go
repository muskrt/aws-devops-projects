package main

import (
	"fmt"

	"github.com/streadway/amqp"
)

func main() {

	fmt.Println("consume application")
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	if err != nil {

		fmt.Println(err)
		panic(err)
	}
	defer conn.Close()
	ch, err := conn.Channel()
	if err != nil {
		fmt.Println(err)
		panic(err)

	}
	defer ch.Close()
	msgs, err := ch.Consume(

		"TestQuee",
		"",
		true,
		false,
		false,
		false,
		nil,
	)
	forever := make(chan bool)
	go func() {
		for d := range msgs {
			fmt.Printf("received message: \"%s\"\n", d.Body)
		}
	}()
	fmt.Println("successfully connected to rabbitmq ")
	fmt.Println("waiting for  messages")
	<-forever

}
