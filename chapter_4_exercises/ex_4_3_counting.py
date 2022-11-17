for number in range(1,21):
	print(number)

count_to_one_million = list(range(1,1_000_001))

print(min(count_to_one_million))
print(max(count_to_one_million))
print(sum(count_to_one_million))

odd_numbers = list(range(1,21,2))
print(odd_numbers)
for odds in odd_numbers:
	print(odds)

threes = list(range(3,31,3))
print(threes)
for number in threes:
	print(number)

cubes = []
for value in range(1,11):
	cube = value ** 3
	cubes.append(cube)
for cube in cubes:
	print(cube)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)
