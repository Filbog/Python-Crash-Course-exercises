from city_country import city_country


def test_normal():
    # city_country("New York", "USA")
    assert city_country("New York", "USA") == "New York, Usa"


# write a test function for city_country
def test_not_capitalized():
    # call the function with a city and country
    # city_country("santiago", "chile")
    # write an assertion that verifies that the function call produces the correct string
    assert city_country("santiago", "chile") == "Santiago, Chile"


# how to run these functions?
