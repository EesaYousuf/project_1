"""Chatbot with Basic Responses
A simple command-line chatbot"""
def chatbot():
    print("Hi! I'm a simple chatbot. Type 'exit' to end.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif 'hello' in user_input:
            print("Bot: Hello! How can I help you?")
        elif 'how are you' in user_input:
            print("Bot: I'm good, thank you!")
        elif 'bye' in user_input:
            print("Bot: Bye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == '__main__':
    chatbot()
