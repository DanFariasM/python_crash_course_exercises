def count_words(filename, word):
    """Count the approximate number of words in a file"""

    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = words.count(word)
        print(f"The file {filename} has the word \"{word}\" about {num_words} times.")


filenames = ["alice.txt", "little_women.txt", "moby_dick.txt", "this_will_not_work.txt", "alice_in_wonderland.txt"]
for filename in filenames:
    count_words(filename, "the")

print("")

with open("moby_dick.txt", encoding="utf-8") as f:
    contents = f.read()
    print(contents.lower().count("the "))