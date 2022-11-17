prompt = "\nPlease tell us what ingredient you want on your pizza"
prompt += "\nEnter 'quit' to exit. "

while True:
    msg = input(prompt)

    if msg == "quit":
        break
    else:
        print(f"Adding {msg} to your pizza!")
