alien = {"color": "green", "speed": "15", "points": "5", "culture": "American"}
# print(alien["points"])
speed_value = alien.get("speed", "no speed value assigned")
# print(speed_value)

for key, value in alien.items():
    print(f"{key} : {value}")


def print_keys():
    print(alien.keys())
    print(sorted(alien.keys()))


# print_keys()


def print_values():
    print(alien.values())
    print(sorted(alien.values()))


# print_values()


def print_items():
    print(alien.items())


# print_items()


def cities():
    cities = {
        "New York": {
            "country": "USA",
            "population": "8.6 million",
            "fact": "The city is the most populous in the United States",
        },
        "London": {
            "country": "England",
            "population": "8.9 million",
            "fact": "The city is the capital of England",
        },
        "Tokyo": {
            "country": "Japan",
            "population": "13.9 million",
            "fact": "The city is the capital of Japan",
        },
    }

    for city_name, city in cities.items():
        print(
            f"{city_name} is a big city in {city['country']} with a population of {city['population']} and a fun fact is {city['fact']}"
        )


cities()

var$1 = 2