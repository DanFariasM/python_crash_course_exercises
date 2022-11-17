glossary = {
    "variable": "Reserved memory location to store values",
    "string": "Series of characters",
    "method": "Action that Python can perform on a piece of data",
    "lists": "Collection of items in a particular order",
    "tuples": "List of items that cannot change",
    "dictionary": "Collection of key-value pairs",
    "loop": "Repeating the same acction with every item",
    "boolean expression": "Conditional test returning True or False",
    }

for term, definition in glossary.items():
    print(f"{term.title()}:")
    print(f"\t{definition}.\n")