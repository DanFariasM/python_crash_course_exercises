# Using every function listed in chapper 3 so far
favorite_games = ["dark souls", "elden ring", "destiny 2", "smash bros", "dragalia lost"]
print(favorite_games)
print(f"My favorite game in Mobile is {favorite_games[-1].title()}")
favorite_games[1] = "demon souls"
print(favorite_games)
favorite_games.append("WoW")
print(favorite_games)
favorite_games.insert(1, "mario kart")
print(favorite_games)
del favorite_games[-1]
print(favorite_games)
print(f"Maybe I should remove {favorite_games.pop(1).title()} from the list, it's not that good")
print(favorite_games)
favorite_games.remove("demon souls")
print(favorite_games)
print(sorted(favorite_games))
print(sorted(favorite_games,reverse=True))
favorite_games.reverse()
print(favorite_games)
favorite_games.sort()
print(favorite_games)
print(f" I have {len(favorite_games)} favorite games")
