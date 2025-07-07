import ChatterBot

# Replace with your own API key
ChatterBot.api_key = "your-api-key"

def smart_chatbot():
    print("Chatbot: Hello! I'm Smart ChatBot. Ask me anything! Type 'bye' to exit.")
    conversation_history = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        # Append user message to history
        conversation_history += f"\nUser: {user_input}\nAI:"

        # Call API
        response = ChatterBot.Completion.create(
            engine="text-davinci-003",  
            prompt=conversation_history,
            max_tokens=150,
            temperature=0.7,
            stop=["User:", "AI:"]
        )

        # Get response text
        answer = response.choices[0].text.strip()
        print("Chatbot:", answer)

        # Append AI response to history
        conversation_history += f" {answer}"

