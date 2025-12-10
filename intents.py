import re

# Patterns for detecting user intent
INTENT_PATTERNS = {
    "greeting": r"\b(hello|hi|hey|good morning|good evening)\b",
    "help": r"\b(help|assist|support|what can you do)\b",
    "small_talk_how_are_you": r"\b(how are you|how’s it going|how do you do)\b",
    "small_talk_who_are_you": r"\b(who are you|what are you)\b",

    # NEW INTENT -> User confused / unsure
    "unsure": r"\b(i don't know|i dont know|i dont have any idea|i don't have any idea|no idea|not sure|idk|nothing)\b",

    "joke": r"\b(joke|tell me a joke)\b",
    "time": r"\b(time now|current time|what time)\b",
    "date": r"\b(today's date|current date|what date)\b",
    "thanks": r"\b(thank you|thanks|thx)\b",
    "exit": r"\b(bye|exit|quit|goodbye)\b"
}

# Responses for each detected intent
INTENT_RESPONSES = {
    "greeting": "Hello! How can I help you today?",
    "help": "I can answer questions, chat with you, and give knowledge-based answers.",
    "small_talk_how_are_you": "I'm doing great! Thanks for asking 😊 How about you?",
    "small_talk_who_are_you": "I'm a simple rule-based chatbot created for your project!",

    # Response when user has no idea what to say
    "unsure": "No worries! 😊 Feel free to ask me anything or tell me what you're trying to understand.",

    "joke": "Why don't programmers like nature? Too many bugs! 😄",
    "thanks": "You're welcome! Happy to help 😊"
}
