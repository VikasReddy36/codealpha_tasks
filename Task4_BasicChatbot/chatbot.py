
def chatbot():
    print("===================================")
    print("       Welcome to AI Chatbot")
    print("===================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input in ["i am fine", "i'm fine", "fine"]:
            print("Bot: That's great to hear!")

        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I'm a simple Python rule-based chatbot.")

        elif user_input in ["what can you do", "help"]:
            print("Bot: I can respond to simple conversations.")

        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()