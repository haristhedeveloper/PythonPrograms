import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Access the API key
groq_api_key = os.getenv("api")

# Now you can use the API key in your requests
from groq import Groq

# Initialize the Groq client with the API key
client = Groq(api_key=groq_api_key)

print("Hello! I am expert in programming fell free to ask or type 'bye' to exit")
# Loop to continuously ask the user for input
while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    # Create a completion request
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "you are expert in programming languages"
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Print the response
    print("Chatbot:", end=" ")
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
    print()  # Move to the next line after printing the response
