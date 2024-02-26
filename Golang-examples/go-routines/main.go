package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup
var mylock sync.Mutex
var count int = 0

func main() {

	channels()
	buffered_channels()
	threadsAndWaitgroups()
	blockingChannel()
	locks()

}
func threadsAndWaitgroups() {
	run := false
	if run {
		start := time.Now()
		defer func() {
			fmt.Println(time.Since(start))
		}()
		for i := 0; i < 50; i++ {
			wg.Add(1)
			go func() {
				time.Sleep(time.Second * 2)
				fmt.Println("spawning enemies")
				wg.Done()
			}()

		}
		wg.Wait()
	}

}
func channels() {
	run := false
	if run {
		human := make(chan bool)
		go func() {
			fmt.Print("Are you human(1) or not(0):")
			var check bool
			fmt.Scan(&check)
			fmt.Println(check)
			human <- check

		}()
		if <-human {
			fmt.Println("There is a human in the area,run for your file")
		} else {
			fmt.Println("You are so lucky dude")
		}
	}

}
func buffered_channels() {
	run := false
	if run {

		safe := make(chan string, 2)
		go func() {
			fmt.Println("You are driving and you wanna make a turn")
			fmt.Print("You should give signal before turn which way left or right: ")
			var signal string
			fmt.Scan(&signal)
			safe <- signal

		}()
		go func() {
			time.Sleep(time.Second * 3)
			fmt.Println("checking if there is no one in the way you wanna turn")
			check := "noone"
			safe <- check

		}()
		direction := <-safe
		if direction == "left" {
			somebody := <-safe
			if somebody == "noone" {
				fmt.Println("You can now turn to the left safely")
			}

		} else if direction == "right" {
			somebody := <-safe
			if somebody == "noone" {
				fmt.Println("You can now turn to the left safely")
			}
		}

	}

}
func blockingChannel() {

	run := false
	if run {

		channel := make(chan string)
		go func(channel chan string) {
			for i := 0; i < 10; i++ {
				fmt.Println("Throwing the ball")
				channel <- "ball"

			}

		}(channel)
		go func(channel chan string) {
			time.Sleep(time.Second * 3)
			life := uint(100)
			for i := 0; i < 9; i++ {
				damage := uint(rand.Intn(100))
				fmt.Printf("You hit %v damage with the %v, life is %v \n", damage, <-channel, life)
				if damage < life {
					life -= damage
				}
				if life == 0 {
					life -= damage
					fmt.Println("You slayed the enemy")
				}
			}

		}(channel)

	}
}

func locks() {
	looth := "100 bullets"
	loothed := false
	run := true
	start := false
	if run {

		for i := 0; i < 1000; i++ {
			go warriors(&start, i, looth, &loothed)
		}
		start = true
		time.Sleep(time.Second * 5)
		fmt.Println(count)

	}
}

func warriors(start *bool, threadnum int, looth string, loothed *bool) {
	for {
		if *start {
			break
		}
	}
	mylock.Lock()
	if !*loothed {
		*loothed = true
		fmt.Printf("warrior %v: I got the looth ,%v\n", threadnum, looth)
	}
	count++
	mylock.Unlock()
}
