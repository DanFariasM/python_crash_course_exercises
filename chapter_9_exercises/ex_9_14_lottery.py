from random import choice

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

winning_ticket = []

for character in range(0,4):
    char = choice(lottery_list)
    winning_ticket.append(char)

print("Any ticket matching these four numbers and letters wins a price:")
print(winning_ticket)

