messages = ['Hello', 'World', '!']
sent_messages = []

def send_messages(messages, sent_messages):
    """Send messages in a list."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)
print(f"Messages: {messages}")
print(f"Sent messages: {sent_messages}")
