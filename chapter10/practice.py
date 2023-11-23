from pathlib import Path


def ex1():
    path = Path("chapter10/programming.txt")
    path.write_text("I love programming!")
    # write_text overwrites content of the file
    path.write_text("I love programming as fuck!")


def guest_book():
    path = Path("chapter10/guest_book.txt")

    guest_list = ""
    while True:
        guest_name = input("name: ")
        if guest_name == "q":
            break
        guest_list += guest_name + "\n"

    path.write_text(guest_list)


# guest_book()


def addition():
    while True:
        n1 = input("n1: ")
        n2 = input("n2: ")
        try:
            result = int(n1) + int(n2)
        except ValueError:
            print("Invalid number or numbers")
        else:
            print(f"The result is: {result}")
            break


# addition()


def cats_and_dogs(*files):
    for file in files:
        path = Path(f"chapter10/cats and dogs/{file}")
        try:
            contents = path.read_text()
        except FileNotFoundError:
            # print("file not found")
            pass
        else:
            print(f"{file.split('.')[0]}:")
            print(contents + "\n")


cats_and_dogs("cats.txt", "dogs.txt")
