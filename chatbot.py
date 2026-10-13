"""Simple rule-based chatbot. No installs needed. Run: python chatbot.py"""
import difflib
import random
from datetime import datetime

BOT_NAME = "Buddy"

# Add your own questions and answers here. Each question can have several replies.
KNOWLEDGE = {
    "hi": ["Hello! How can I help you?", "Hi there! What would you like to know?"],
    "hello": ["Hello! How can I help you?", "Hey! Ask me anything basic."],
    "how are you": ["I'm doing great, thanks for asking! How about you?"],
    "what is your name": [f"I'm {BOT_NAME}, a simple chatbot."],
    "who made you": ["I was built as a Python project in VS Code."],
    "what can you do": ["I can answer basic questions, tell the time and date, and chat a little."],
    "what is python": ["Python is a popular, beginner-friendly programming language."],
    "what is ai": ["AI (Artificial Intelligence) is when machines do tasks that normally need human intelligence."],
    "what is a chatbot": ["A chatbot is a program that talks with people using text or voice."],
    "what is the capital of india": ["The capital of India is New Delhi."],
    "what is the capital of france": ["The capital of France is Paris."],
    "what is the capital of japan": ["The capital of Japan is Tokyo."],
    "what is the capital of the united states": ["The capital of the United States is Washington, D.C."],
    "what is the largest planet": ["Jupiter is the largest planet in our solar system."],
    "what is the red planet": ["Mars is often called the Red Planet."],
    "how many days are in a week": ["There are seven days in a week."],
    "what is the boiling point of water": ["At sea level, water boils at 100 degrees Celsius (212 degrees Fahrenheit)."],
    "what is 2 plus 2": ["2 plus 2 equals 4."],
    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer get cold? It left its Windows open.",
    ],
    "thanks": ["You're welcome!", "Happy to help!"],
    "thank you": ["You're welcome!", "Anytime!"],
    "bye": ["Goodbye! Have a great day!"],
}


def special_answers(text):
    """Answer questions whose answers change (the current time and date)."""
    time_questions = ("what time is it", "what is the time", "current time", "tell me the time")
    date_questions = ("what is the date", "what is today's date", "current date", "tell me the date")

    if "time" in text or difflib.get_close_matches(text, time_questions, n=1, cutoff=0.75):
        return "The time is " + datetime.now().strftime("%I:%M %p")
    if ("date" in text or "today" in text
            or difflib.get_close_matches(text, date_questions, n=1, cutoff=0.75)):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y")
    return None


def get_reply(user_input):
    text = user_input.lower().strip().rstrip("?! .")

    special = special_answers(text)
    if special:
        return special

    # Find the closest known question (tolerates small typos)
    match = difflib.get_close_matches(text, KNOWLEDGE.keys(), n=1, cutoff=0.6)
    if match:
        return random.choice(KNOWLEDGE[match[0]])

    return "Sorry, I don't know that yet. Try asking something else!"


def main():
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        reply = get_reply(user_input)
        print(f"{BOT_NAME}: {reply}")
        if user_input.lower().rstrip("!?.") == "bye":
            break


if __name__ == "__main__":
    main()
