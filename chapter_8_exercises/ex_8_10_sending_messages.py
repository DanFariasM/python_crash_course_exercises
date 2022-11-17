def send_messages(messages_in, sent_messages):
    """Prints a list of messages"""
    while messages_in:
        outgoing_message = messages_in.pop()
        print(f"Sending message: {outgoing_message}")
        sent_messages.append(outgoing_message)

message_list = ["Hello", "keep going!", "don't give up!"]
messages_sent = []

send_messages(message_list, messages_sent)

print(message_list)
print(messages_sent)