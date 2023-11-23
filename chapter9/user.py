class User:
    def __init__(self, first_name, last_name, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} likes {self.hobby}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts: {self.login_attempts}")


class Privileges:
    def __init__(self):
        self.privileges = ["can ban users", "can delete posts", "can see details"]

    def display_privileges(self):
        print("This user can:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, hobby, type):
        super().__init__(first_name, last_name, hobby)
        self.type = type
        self.privileges = Privileges()

    def display_type(self):
        print(f"type: {self.type}")
