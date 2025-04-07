def chatbotresponse(userinput):
    userinput = userinput.lower()

    
    greetings = ["hello", "hi", "hey", "greetings"]
    if userinput in greetings:
        return "Hello! How can I assist you today?"


    
    if "how are you" in userinput:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in userinput:
        return "I am ChatBot, your virtual assistant!"
    elif "help" in userinput:
        return "how can I help U?"
    
    
    return "Can you ask something else?"


print("AI Chatbot: 'bye' to exit.")
while True:
    user_input = input()
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbotresponse(user_input)
    print(f"Chatbot: {response}")