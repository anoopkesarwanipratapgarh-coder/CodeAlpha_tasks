def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user = input("You: ").strip().lower()

        if user in ["hello", "hi", "hey"]:
            print("Chatbot: Hi!")

        elif user in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks!")

        elif user in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

#RUN CHAT BOT
if __name__ == "__main__":
    chatbot()

      