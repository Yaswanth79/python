def respond(message):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm good, thank you!",
        "bye": "Goodbye!",
    }
    return responses.get(message.lower(), "I don't understand that.")

if __name__ == "__main__":
    print("Chatbot: Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {respond(user_input)}")
