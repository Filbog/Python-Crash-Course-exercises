from pathlib import Path
import json


def get_fav_num(path):
    fav_num = input("What is your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print("thx \n")


def read_fav_num(path):
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number! It's {fav_num}")


def fav_num():
    path = Path("chapter10/fav_number/fav_num.json")
    if path.exists():
        read_fav_num(path)
    else:
        get_fav_num(path)


fav_num()
