def pizza_toppings():
    active = True
    while active:
        topping = input("Enter a topping: ")
        if topping == "quit":
            active = False
        else:
            print("I'll add " + topping + " to your pizza.")


# pizza_toppings()


def movie_tickets_if():
    print("Movie Tickets = if statement version")
    age = ""

    while age != "quit":
        age = input("What's your age?")
        if age != "quit":
            age = int(age)
            if age < 3:
                print("The ticket is free")
            elif age <= 12:
                print("The ticket is 10$")
            else:
                print("The ticket is 15$")


movie_tickets_if()


def movie_tickets_break():
    while True:
        age = input("What's your age? ")
        if age == "quit":
            break
        else:
            age = int(age)
            if age < 3:
                print("The ticket is free")
            elif age <= 12:
                print("The ticket is 10$")
            else:
                print("The ticket is 15$")


# movie_tickets_break()


def movie_tickets_flag():
    active = True
    while active:
        age = input("What's your age?")
        if age == "quit":
            active = False
        else:
            age = int(age)
            if age < 3:
                print("The ticket is free")
            elif age <= 12:
                print("The ticket is 10$")
            else:
                print("The ticket is 15$")


# movie_tickets_flag()
