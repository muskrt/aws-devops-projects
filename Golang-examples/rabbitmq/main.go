package main

import (
	"fmt"

	"github.com/streadway/amqp"
)

func main() {

	fmt.Println("rabbitmq test on mars")
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	if err != nil {
		fmt.Println(err)
		panic(err)

	}
	defer conn.Close()
	fmt.Println("successfully connected to rabbit")
	ch, err := conn.Channel()
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	defer ch.Close()
	q, err := ch.QueueDeclare(
		"TestQuee",
		false,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	fmt.Println(q)
	err = ch.Publish(
		"",
		"TestQuee",
		false,
		false,
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        []byte("hello world"),
		},
	)
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	fmt.Println("successfully published to quee")
}
