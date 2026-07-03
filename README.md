# Task 1 - Rule-Based Chatbot (CodBot)

**CodSoft AI Internship**

## About
CodBot is a simple rule-based chatbot built in Python. It uses **regex pattern
matching** to identify the intent behind a user's message and responds with a
predefined, appropriate reply — no machine learning involved, just careful
rule design.

## How it works
- Each "rule" pairs a set of regex patterns with a set of possible responses.
- User input is lowercased and checked against each rule's patterns using `re.search`.
- On a match, a response is chosen randomly from that rule's response list (to
  avoid the bot sounding repetitive).
- If no rule matches, a random fallback message is shown.

## Features
- Greetings, small talk, asking the bot's name
- Tells the current time and date
- Tells a joke
- Graceful exit on words like "bye" / "exit" / "quit"

## How to run
```bash
python3 chatbot.py
```

Then just type messages at the `You:` prompt. Type `bye` to exit.

## Example conversation
```
CodBot: Hello! I'm CodBot. Type 'bye' anytime to exit.

You: hi
CodBot: Hi there! What can I do for you?

You: what is your name
CodBot: I'm CodBot, a rule-based chatbot built for the CodSoft AI Internship.

You: tell me a joke
CodBot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
CodBot: Goodbye! Have a great day.
```

## Tech used
- Python 3
- `re` module (regex pattern matching)

---
Part of the CodSoft Artificial Intelligence Internship (Task 1 of 5).
