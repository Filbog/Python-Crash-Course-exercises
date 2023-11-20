def famous_quote():
    name = "   Bob Dylan   "
    quote = "    'All I can do is be me, whoever that is.'"
    print(f"{quote.strip()} - {name.strip()}")


# famous_quote()


def remove_extension():
    filename = "notes.txt"
    print(filename.removesuffix(".txt"))


# remove_extension()


def numbers():
    very_big_num = 14_000_000_000
    print(very_big_num)
    # assign multiple values in one line
    x, y, z = 10, 15, 3
    print(y)
    print(x, y, z)


# numbers()


def zen_of_python():
    import this

    print(this)


# zen_of_python()
