from restaurant import Restaurant
from ice_cream_stand import IceCreamStand

import user as u


# def user_exercise_tests():
# new_user = User("john", "doe", "programming")
# new_user.describe_user()
# new_user.greet_user()
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# new_user.reset_login_attempts()


def user_ex_tests():
    new_admin = u.Admin("John", "Doe", "skiing", "content moderator")
    new_admin.privileges.display_privileges()
    new_admin.display_type()


# user_ex_tests()


def restaurant_exercise_tests():
    kfc = Restaurant("KFC", "Miesna")
    kfc.describe_retaurant()
    print(kfc.number_served)
    kfc.number_served = 10
    print(kfc.number_served)
    kfc.set_number_served(15)
    print(kfc.number_served)
    kfc.increment_number_served(5)
    print(kfc.number_served)
    kfc.increment_number_served(-10)
    print(kfc.number_served)


# restaurant_exercise_tests()


def ice_cream_stand_ex_tests():
    my_stand = IceCreamStand("My Stand", "Ice Cream")
    my_stand.display_flavors()


# ice_cream_stand_ex_tests()
