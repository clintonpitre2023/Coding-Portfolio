# Simple Python Chatbot

def chatbot():
    # Dictionary to store predefined questions and responses
    responses = {
        "hi": "Hello there!",
        "how are you?": "I'm doing well, thank you!",
        "what is your name?": "I am a simple chatbot created in Python.",
        "bye": "Goodbye! Have a great day!"
    }

    # Chatbot greeting
    print("Hello! I am a chatbot. How can I help you?")
    
    while True:
        # Take input from the user
        user_input = input("You: ").strip().lower()
        
        # Check if the user wants to exit the chat
        if user_input == "bye":
            print(responses.get(user_input, "I'm not sure how to respond to that."))
            break
        
        # Print an appropriate response from the dictionary
        print("Chatbot:", responses.get(user_input, "I'm not sure how to respond to that."))

if __name__ == "__main__":
    chatbot()
