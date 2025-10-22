import os
import google.generativeai as genai

# Secure API key handling
api_key = os.getenv("AIzaSyCoTMxTlgPTs0laMqpf7LNcYA2-xlkApVU")  # Set this in your system environment variables
genai.configure(api_key=api_key)

# Chatbot personality
basic_info = """You are a friendly chatbot named 'HeyBuddy'.
You always greet the user with 'Namaste' and ask about how they are doing.
Provide helpful responses while maintaining a positive and engaging tone.
"""

# Predefined keyword responses
instructions = {
    "study": "How's college going?",
    "motivation": "You're doing great! Keep pushing forward! 🚀",
    "joke": "Why don’t scientists trust atoms? Because they make up everything! 😆",
}

# Initialize AI model
model = genai.GenerativeModel("gemini-pro", system_instruction=basic_info)

# Function to check predefined responses
def get_instruction(user_input):
    user_input = user_input.lower()
    for keyword, response in instructions.items():
        if keyword in user_input:
            return response
    return None

# Function to handle chatbot interaction
def chatbot():
    print("HeyBuddy: Namaste! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("HeyBuddy: Goodbye! Have a great day! 😊")
            break

        # Check if user input matches predefined instructions
        instruction_response = get_instruction(user_input)
        if instruction_response:
            print("HeyBuddy:", instruction_response)
            continue

        # Otherwise, generate AI response
        try:
            response = model.generate_content(user_input)
            print("HeyBuddy:", response.text)
        except Exception as e:
            print("HeyBuddy: Oops! Something went wrong. Please try again later.")

# Run the chatbot
chatbot()
