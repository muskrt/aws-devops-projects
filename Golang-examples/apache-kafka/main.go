package main

import (
	"encoding/json"
	"fmt"
	"log"
	"time"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

var topic string = "DEVOPS"

type Data struct {
	Name     string
	Lastname string
	Age      string
}

type OrderPlacer struct {
	producer   *kafka.Producer
	topic      string
	deliverych chan kafka.Event
}

func NerOrderPlacer(p *kafka.Producer, topic string) *OrderPlacer {

	return &OrderPlacer{
		producer:   p,
		topic:      topic,
		deliverych: make(chan kafka.Event, 10000),
	}
}

func (op *OrderPlacer) placeOrder(orderType string, size int) error {
	var (
		format  = fmt.Sprintf("%s - %d", orderType, size)
		payload = []byte(format)
	)
	err := op.producer.Produce(
		&kafka.Message{
			TopicPartition: kafka.TopicPartition{Topic: &op.topic, Partition: 0},
			Value:          payload},
		op.deliverych,
	)

	if err != nil {
		log.Fatal(err)

	}
	<-op.deliverych
	fmt.Println("message sended")

	return nil
}

func main() {
	go_on := ""
	message := Data{
		Name:     "mustafa",
		Lastname: "kurt",
		Age:      "30",
	}
	jsonData, err := json.Marshal(message)
	if err != nil {
		fmt.Println(err)
	}
	go consumer()
	for {
		producer(string(jsonData))
		fmt.Println("consumer running in parallel")
		fmt.Println("Exit the program(1) or continue (2):")
		fmt.Scan(&go_on)
		if go_on == "1" {
			break
		}

	}

}

func producer(message string) {

	p, err := kafka.NewProducer(&kafka.ConfigMap{

		"bootstrap.servers": "localhost:9092",
		"client.id":         "somethings",
		"acks":              "all"})
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	op := NerOrderPlacer(p, "DEVOPS")

	if err := op.placeOrder(message, 1); err != nil {
		log.Fatal(err)
	}
	time.Sleep(time.Second * 3)

}

func consumer() {

	consumer, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": "localhost:9092",
		"group.id":          "somethings",
		"auto.offset.reset": "smallest"})
	if err != nil {

		log.Fatal(err)
	}
	err = consumer.Subscribe(topic, nil)
	if err != nil {
		log.Fatal(err)
	}
	for {

		ev := consumer.Poll(100)
		switch e := ev.(type) {
		case *kafka.Message:
			fmt.Printf("message is: %s\n", string(e.Value))
		case *kafka.Error:
			fmt.Printf("%v\n", e)

		}
	}

}
