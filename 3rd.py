# Task 8: Create a Simple Chatbot (CLI)
# Explanation:
# • Build a basic rule-based chatbot
# • Use if-elif statements to respond to greetings, FAQs, etc.

print("Simple Chatbot")
print("Type 'bye' to exit the chat.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: I am a simple Python chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")