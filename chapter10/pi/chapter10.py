from pathlib import Path

path = Path("chapter10/pi/pi_file.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

my_birthday = "070596"

if my_birthday in pi_string:
    index = pi_string.index(my_birthday)
    print(f"Your birthday appears in the first million digits of pi at index: {index}")
