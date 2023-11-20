def list_comprehension():
    plus_ten = [n + 10 for n in range(1, 11)]
    print(plus_ten)


def multiples_of_3():
    multi = [n for n in range(3, 31, 3)]
    print(multi)


# multiples_of_3()


def cube_comp():
    cubes = [n**3 for n in range(1, 11)]
    print(cubes)


cube_comp()
