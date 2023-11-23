class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_retaurant(self):
        print(
            f"The restaurant name is {self.restaurant_name.title()}. It serves {self.cuisine_type} cuisine"
        )

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        if num > 0:
            self.number_served += num
        else:
            print("invalid number")
