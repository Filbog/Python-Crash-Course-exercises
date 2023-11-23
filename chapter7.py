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


# movie_tickets_if()


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


def sandwiches():
    sandwich_orders = [
        "ham and cheese",
        "cheese",
        "pastrami",
        "chicken",
        "avocado",
        "gyros",
        "pastrami",
        "peanut butter",
        "pastrami",
    ]
    finished_sandwiches = []

    # We've run out of pastrami!
    print("We've run out of pastrami!")
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")

    for sandwich in sandwich_orders:
        print(f"Your {sandwich} sandwich is ready!")
        finished_sandwiches.append(sandwich)

    print("Following sandwiches have beeen made: ")
    for finished in finished_sandwiches[:-1]:
        print(f"{finished.title()},")
    print(f"{finished_sandwiches[-1]}.")


# sandwiches()


def vacation():
    poll = {}
    active = True

    while active:
        name = input("What's your name?")
        dream_vacation = input("Where would you go for you dream vacation?")
        next_responds = input("Would you like another person to respond? (yes/no)")
        poll[name] = dream_vacation
        if next_responds.lower() == "no":
            active = False
    print("Polling complete. Here are the results:")
    for name, vacation in poll.items():
        print(f"{name.title()} would love to go to {vacation.title()}")


vacation()
