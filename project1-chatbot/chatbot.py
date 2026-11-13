# ==========================================================
# DECODLABS AI PROJECT 1
# RULE-BASED AI CHATBOT
# Developed using Python
# ==========================================================

import string


# ==========================================================
# 1. PREDEFINED CHATBOT RESPONSES
# ==========================================================

responses = {

    # Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Welcome to DecodLabs AI.",
    "hey": "Hey! What would you like to know?",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! What can I help you with?",
    "good evening": "Good evening! Welcome to DecodLabs AI.",

    # General conversation
    "how are you": "I'm functioning perfectly! Thanks for asking.",
    "thank you": "You're welcome! I'm happy to help.",

    # Chatbot information
    "what is your name": "I am the DecodLabs Rule-Based AI Chatbot.",
    "who created you": "I was created as a rule-based chatbot project using Python.",
    "what can you do": (
        "I can respond to greetings, answer predefined questions, "
        "and provide basic information about AI."
    ),

    # Artificial Intelligence
    "what is ai": (
        "Artificial Intelligence enables computers to perform "
        "tasks that typically require human intelligence."
    ),

    "what is artificial intelligence": (
        "Artificial Intelligence is the field of computer science "
        "that focuses on creating systems capable of performing "
        "tasks that typically require human intelligence."
    ),

    "what is machine learning": (
        "Machine Learning is a branch of AI that enables systems "
        "to learn patterns from data."
    ),

    # Programming
    "what is python": (
        "Python is a popular programming language used in web "
        "development, automation, data science, and AI."
    ),

    # Assistance
    "help": (
        "You can greet me, ask about AI, ask my name, "
        "learn about Python, or type 'exit' to end the conversation."
    )
}


# ==========================================================
# 2. EXIT COMMANDS
# ==========================================================

exit_commands = {"exit", "quit", "bye", "goodbye"}


# ==========================================================
# 3. INPUT SANITIZATION
# ==========================================================

def sanitize_input(user_input):

    # Convert input to lowercase and remove extra spaces
    clean_input = user_input.lower().strip()

    # Remove punctuation
    clean_input = clean_input.translate(
        str.maketrans("", "", string.punctuation)
    )

    return clean_input


# ==========================================================
# 4. CHATBOT RESPONSE ENGINE
# ==========================================================

def get_response(user_input):

    # Sanitize user input
    clean_input = sanitize_input(user_input)

    # Handle empty input
    if not clean_input:
        return "Please enter a message so I can help you."

    # Check exit commands
    if clean_input in exit_commands:
        return None

    # Exact match lookup using .get()
    reply = responses.get(clean_input)
    if reply:
        return reply

    # Split input into individual words
    words = clean_input.split()

    # Keyword recognition (specific topics first)
    if "artificial intelligence" in clean_input:
        return (
            "Artificial Intelligence is the field of computer science "
            "that focuses on creating systems capable of performing "
            "tasks that typically require human intelligence."
        )

    if "machine learning" in clean_input:
        return (
            "Machine Learning is a branch of Artificial Intelligence "
            "that allows computers to learn patterns from data."
        )

    if "your name" in clean_input:
        return "I am the DecodLabs Rule-Based AI Chatbot."

    if "python" in words:
        return (
            "Python is a popular programming language used in "
            "automation, software development, data science, and AI."
        )

    # Greeting recognition (checked last so topics win)
    if any(word in words for word in ["hello", "hi", "hey"]):
        return (
            "Hello! Welcome to DecodLabs AI. "
            "How can I assist you?"
        )

    # Fallback for unknown inputs
    return (
        "I'm sorry, I don't understand that yet. "
        "Try greeting me, asking about AI, or typing 'help'."
    )


# ==========================================================
# 5. MAIN CHATBOT FUNCTION
# ==========================================================

def run_chatbot():

    print("\n" + "=" * 50)
    print("          DECODLABS AI CHATBOT")
    print("=" * 50)

    print("\nBot: Hello! Welcome to DecodLabs AI.")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'exit', 'quit', or 'bye' to stop.\n")

    # Continuous conversation loop
    while True:

        try:

            # Receive user input
            user_input = input("You: ")

            # Generate chatbot response
            response = get_response(user_input)

            # Check whether the user wants to exit
            if response is None:

                print("\nBot: Goodbye! Thanks for chatting with me.")
                print("Chatbot terminated.\n")

                break

            # Display chatbot response
            print("Bot:", response)

        except KeyboardInterrupt:

            print("\n\nBot: Chat interrupted. Goodbye!")
            break

        except EOFError:

            print("\n\nBot: Input stream closed. Goodbye!")
            break

        except Exception as error:

            print("Bot: Something went wrong. Please try again.")
            print("Error:", error)


# ==========================================================
# 6. PROGRAM ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    run_chatbot()