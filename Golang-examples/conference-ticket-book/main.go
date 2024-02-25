package main

import (
	"fmt"
	"strings"
)

var name = "Go conference"
var conferenceTickets uint = 50
var remainingTickets uint = 50
var bookings = make([]userData, 0)
var firstName string
var lastName string
var email string
var userTickets uint

type userData struct {
	firstName       string
	lastName        string
	email           string
	numberOfTickets uint
}

func main() {

	greetusers()
	for remainingTickets > 0 && len(bookings) < 50 {

		getUserInput()
		validRequest := ValidateUserInput()

		if validRequest {
			bookTicket()
			fmt.Printf("%v tickets remaining for %v\n", remainingTickets, conferenceTickets)
			firstNames := getFirstNames()
			fmt.Printf("The first names of bookings are: %v\n", firstNames)
			if remainingTickets == 0 {
				fmt.Println("Our conference is booked out. Come back next year")
				break
			}

		} else {
			fmt.Printf("your input is invalid try again ")

		}
	}
}

func greetusers() {

	fmt.Printf("welcome to %v booking application\n", name)
	fmt.Printf("we have total of %v , tickets and %v are still available\n", conferenceTickets, remainingTickets)
	println("Get your tickets here to attend")
}

func getFirstNames() []string {

	firstNames := []string{}
	for _, booking := range bookings {
		firstNames = append(firstNames, booking.firstName)
	}
	return firstNames

}

func getUserInput() {

	fmt.Println("Enter your first name:")
	fmt.Scan(&firstName)

	fmt.Println("Enter your last name:")
	fmt.Scan(&lastName)

	fmt.Println("Enter your email :")
	fmt.Scan(&email)

	fmt.Println("Enter number of tickets:")
	fmt.Scan(&userTickets)

}

func bookTicket() {

	remainingTickets = remainingTickets - userTickets

	var userData = userData{
		firstName:       firstName,
		lastName:        lastName,
		email:           email,
		numberOfTickets: userTickets,
	}
	bookings = append(bookings, userData)

	fmt.Printf("The whole array: %v\n", bookings)

	fmt.Printf("Thank you %v %v for booking %v tickets. You will receive a confirmation email at %v\n",
		firstName, lastName, userTickets, email)
}
func ValidateUserInput() bool {

	isValidName := len(firstName) >= 2 && len(lastName) >= 2
	isValiedEmail := strings.Contains(email, "@")
	isValidTicketNumber := userTickets > 0 && userTickets <= remainingTickets

	return isValidName && isValiedEmail && isValidTicketNumber
}
