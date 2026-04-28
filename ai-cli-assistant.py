import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# This list holds the conversation history
conversation_history = []

# Function to handle chat interactions
def chat(user_message):
    """Send a message to the Groq API and get a response."""
    
    # 1. Add user message to history
    conversation_history.append({
        "role": "user", 
        "content": user_message
    })
    
    # 2. Define the System prompt (Usually stays at index 0)
    system_prompt = {
        "role": "system", 
        "content": "You are an AI assistant. Be concise and helpful."
    }
    
    try:
        # 3. FIXED: Added comma after model and moved system prompt to the front
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[system_prompt] + conversation_history
        )
        
        ai_reply = response.choices[0].message.content
        
        # 4. Add assistant's response to history
        conversation_history.append({
            "role": "assistant",
            "content": ai_reply
        })
        
        return ai_reply
    
    # 5. Handle potential errors gracefully
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        return "Sorry, something went wrong while processing your request."


# Main function to run the CLI assistant
def main():
    print("Welcome to the AI CLI Assistant! (Powered by Groq)")
    print("Type 'quit' or 'exit' to stop. \n")
    
    # Loop to continuously get user input
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Skip empty input
        if not user_input:
            continue
        
        # Exit condition
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! Have a great day!")
            break
        
        # Get and print the AI's response
        print("AI: ", end="", flush=True)
        ai_response = chat(user_input)
        print(ai_response)
        print()  # Add a newline for better readability
        
        
if __name__ == "__main__":
    main()