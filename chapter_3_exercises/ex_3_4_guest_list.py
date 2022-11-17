guest_list = ["mama",  "papa", "MT", "abuela"]
print(f"Do you want to come have dinner, {guest_list[0].title()}?")
print(f"Maybe we can invite {guest_list[1].title()} and {guest_list[3].title()} as well!")
print(f"{guest_list[2]} and I will cook")

# Changing guest list
print(f"seems like {guest_list[-1].title()} can't make it")
guest_list[-1] = "tia"
print(f"Do you want to come have dinner {guest_list[0].title()}?\nDo you want to come have dinner {guest_list[1].title()}?\nDo you want to come have dinner {guest_list[2].title()}?\nDo you want to come have dinner {guest_list[3].title()}?")

# more guests
print(f" Hey {guest_list}, I found a bigger table!")
guest_list.insert(0,"jose")
guest_list.insert(2,"hugo")
guest_list.append("jorge")
print(f"Lots of people coming! Inviting {guest_list}!")

# Shrinking guest list
print("Sorry guys, I can only invite two people")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Hey {guest_list[0].title()}, you are still invited!")
print(f"Hey {guest_list[1].title()}, you are still invited!")
del guest_list[1]
del guest_list[0]
print(guest_list)

# Back from excercise 3-8
print(len(guest_list))
