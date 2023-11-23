def make_shirt(text="I love Python", size="L"):
    print(f"Shirt with text '{text}' of size {size} is done ")


# make_shirt("Hiii", "XS")
# make_shirt(size="XL", text="Hello")
# make_shirt(size="M")
# make_shirt(text="I hate CSS")


def new_album(album_name, artist_name, number_of_songs=None):
    return {
        "album": album_name,
        "artist": artist_name,
        "number of songs": number_of_songs,
    }


def make_albums():
    album_list = []
    for _ in range(0, 3):
        album = input("album: ")
        artist = input("artist: ")
        are_songs = input("Do you want to pass in number of songs? (y/n): ")
        if are_songs == "y":
            songs = input("please enter number of songs")
            album_list.append(new_album(album, artist, songs))
        else:
            album_list.append(new_album(album, artist))
    print(album_list)


# make_albums()


def sandwiches(*toppings):
    for topping in toppings:
        print(topping)


# sandwiches("hello", "hi", "sdas", "qwerty")
# sandwiches("fifi", "fefe", "bebe" "ebe")


def build_profile(first, last, **user_info):
    print(user_info)
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info


user_profile = build_profile("Ff", "bog", gender="male", sex="no")
print(user_profile)
