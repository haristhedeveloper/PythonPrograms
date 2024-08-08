def chatbot_response(user_input):
  
    user_input = user_input.lower()

   
    rules = {
        'hello': 'Hello! How can I help you today?',
        'hi': 'Hi there! How can I assist you?',
        'bye': 'Goodbye! Have a great day!',
        'thank you': 'You are welcome!',
        'thanks': 'You are welcome!',
        'how are you': 'I am a bot, but I am functioning as expected!',
        'help': 'Sure, how can I help you?'
    }


    for keyword in rules:
        if keyword in user_input:
            return rules[keyword]


    return "I'm sorry, I didn't understand that. Can you please rephrase?"
print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
