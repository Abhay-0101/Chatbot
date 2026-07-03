"""
CodBot - A Rule-Based Chatbot
CodSoft AI Internship - Task 1

This chatbot uses regex pattern matching to identify the intent behind
a user's message and respond with a predefined, appropriate reply.
No AI/ML model is used here — just careful pattern design, which is
exactly what Task 1 asks for (if-else / pattern matching techniques).
"""

import re
import random
from datetime import datetime

# ---------------------------------------------------------------------
# 1. Define response rules
#    Each rule = a list of regex patterns + a list of possible responses
#    Using a list of responses (chosen randomly) makes the bot feel
#    less robotic and repetitive.
# ---------------------------------------------------------------------

RULES = [
    {
        "patterns": [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bgood morning\b", r"\bgood evening\b"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to see you here."
        ]
    },
    {
        "patterns": [r"\bhow are you\b", r"\bhow're you\b", r"\bhow you doing\b"],
        "responses": [
            "I'm just a program, but I'm running smoothly! How about you?",
            "Doing great, thanks for asking! How can I help?"
        ]
    },
    {
        "patterns": [r"\bwhat is your name\b", r"\bwho are you\b", r"\byour name\b"],
        "responses": [
            "I'm CodBot, a rule-based chatbot built for the CodSoft AI Internship.",
            "You can call me CodBot!"
        ]
    },
    {
        "patterns": [r"\btime\b"],
        "responses": [
            f"The current time is {datetime.now().strftime('%H:%M:%S')}."
        ]
    },
    {
        "patterns": [r"\bdate\b", r"\btoday'?s date\b"],
        "responses": [
            f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."
        ]
    },
    {
        "patterns": [r"\bhelp\b", r"\bwhat can you do\b"],
        "responses": [
            "I can chat with you about basic topics — try asking my name, "
            "the time, the date, or just say hello!"
        ]
    },
    {
        "patterns": [r"\bjoke\b"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I would tell you a UDP joke, but you might not get it."
        ]
    },
    {
        "patterns": [r"\bthank(s| you)\b"],
        "responses": [
            "You're welcome!",
            "Anytime! Happy to help."
        ]
    },
    {
        "patterns": [r"\bbye\b", r"\bgoodbye\b", r"\bsee you\b", r"\bquit\b", r"\bexit\b"],
        "responses": [
            "Goodbye! Have a great day.",
            "See you later!"
        ]
    },
]

# Fallback responses when no rule matches
FALLBACKS = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I don't have an answer for that yet.",
    "Sorry, I didn't quite get that. Try asking something else!"
]

EXIT_WORDS = {"bye", "goodbye", "quit", "exit", "see you"}


def get_response(user_input: str) -> str:
    """
    Match the user's input against known patterns (case-insensitive)
    and return an appropriate response. Falls back to a default
    message if nothing matches.
    """
    text = user_input.lower().strip()

    for rule in RULES:
        for pattern in rule["patterns"]:
            if re.search(pattern, text):
                return random.choice(rule["responses"])

    return random.choice(FALLBACKS)


def chat():
    """Runs the chatbot in a simple command-line loop."""
    print("CodBot: Hello! I'm CodBot. Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        response = get_response(user_input)
        print(f"CodBot: {response}")

        if any(word in user_input.lower() for word in EXIT_WORDS):
            break


if __name__ == "__main__":
    chat()
