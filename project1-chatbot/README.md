# Rule-Based AI Chatbot

## Description
A rule-based chatbot built in Python for the DecodeLabs AI internship. It cleans user input, looks up answers in a dictionary of 15+ intents, falls back gracefully on unknown input, and exits on a command like "bye".

## Features
- Input sanitization (case, spaces, punctuation)
- Dictionary-based responses with `.get()`
- Continuous conversation loop with a clean exit

## How to Run
```
python chatbot.py
```
Type `help` to see what the bot can answer, and `bye` to quit.