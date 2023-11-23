from pathlib import Path
import json


def get_stored_user(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_user(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    user = {"username": username, "first_name": first_name, "last_name": last_name}
    contents = json.dumps(user)
    path.write_text(contents)
    return user


def greet_user():
    """Greet the user by name."""
    path = Path("chapter10/user/username.json")
    user = get_stored_user(path)
    if user:
        is_correct = input(f"Are you {user['username']}? (y/n) ")
        if is_correct == "y":
            print(f"Welcome back, {user['username']}!")
            print(
                f"Your first name is {user['first_name']}. Your last name is {user['last_name']}."
            )
        else:
            user = get_new_user(path)
            print(f"We'll remember you when you come back, {user['username']}!")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")


greet_user()
