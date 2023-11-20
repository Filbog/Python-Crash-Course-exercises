def guest_list_exercise():
    guest_list = ["Bob Dylan", "Socrates", "Slavoj Zizek", "Angela Yu"]
    first_out = guest_list.pop(2)
    print(f"Sorry {first_out.split(' ')[0]}, you can't come to my dinner after all :(")
    print(guest_list, "\n **************")
    awkward = "Bob Dylan"
    second_out = guest_list.remove(awkward)
    print(f"Sorry {awkward.split(' ')[0]}, you're too awkward for my dinner")
    print(guest_list, "\n **************")


# guest_list_exercise()


def sorting():
    places_to_visit = ["Great Wall", "Joshua Tree", "Mount Everest", "Maledives"]
    places_to_visit.reverse()
    print(places_to_visit)
    places_to_visit.reverse()
    print(places_to_visit)


sorting()
