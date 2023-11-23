from random import randint

available_chars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]


def lottery():
    winning_chars = ""
    av_chars_copy = available_chars[:]
    for n in range(0, 4):
        # print(av_chars_copy)
        random_char = str(av_chars_copy.pop(randint(0, len(av_chars_copy) - 1)))
        # print(random_char)
        winning_chars += random_char

    # print(f"{winning_chars} wins a prize")
    return winning_chars


my_ticket = "2a6d"
counter = 0

winning_ticket = lottery()
while my_ticket != winning_ticket:
    counter += 1
    winning_ticket = lottery()

print(counter)
