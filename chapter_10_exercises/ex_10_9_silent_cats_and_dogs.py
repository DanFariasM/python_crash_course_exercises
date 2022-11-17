filename = "cats.txt"

try:
    with open(filename) as f:
        contents = f.readlines()
except FileNotFoundError:
    pass
else:
    for line in contents:
        print(line.strip())


filename = "dogs.txt"

try:
    with open(filename) as f:
        contents = f.readlines()
except FileNotFoundError:
    pass
else:
    for line in contents:
        print(line.strip())