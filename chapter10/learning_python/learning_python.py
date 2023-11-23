from pathlib import Path

path = Path("chapter10/learning_python/learned.txt")

contents = path.read_text()

# print(contents)
# print(contents.splitlines())

# learned_list = [line for line in contents.splitlines()]
# print(learned_list)
for line in contents.splitlines():
    line = line.strip().replace(" ", "_")
    print(line)
