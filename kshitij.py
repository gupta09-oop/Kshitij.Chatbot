import google.generativeai as genai
import os

# Configure API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API Key not found. Set GEMINI_API_KEY as an environment variable.")

genai.configure(api_key=API_KEY)

# Use the correct model name from the available list
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Change if needed
chat = model.start_chat()

print("Chatbot is ready! Type 'exit' to stop.")

while True:
    message = input("You: ")
    if message.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    # Custom responses
    if "who made you" in message or "who created you" in message:
        print("Chatbot: I was created by Kshitij Gupta! 😊")
        continue
    try:
        response = chat.send_message(message)
        print("Chatbot:", response.text)
    except Exception as e:
        print("Error:", e)
