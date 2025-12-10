import re
from datetime import datetime
from intents import INTENT_PATTERNS, INTENT_RESPONSES
from utils import log, load_kb, fuzzy_search, bot_say, start_conversation_log, end_conversation_log

knowledge_base = load_kb()


def detect_intent(user_input):
    for intent, pattern in INTENT_PATTERNS.items():
        if re.search(pattern, user_input.lower()):
            return intent
    return None


def handle_intent(intent):
    if intent in INTENT_RESPONSES:
        return INTENT_RESPONSES[intent]

    if intent == "time":
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    if intent == "date":
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    if intent == "exit":
        return "Goodbye! Have a great day! 😊"

    return None


def knowledge_lookup(user_input):
    words = user_input.lower().split()

    # Fuzzy match whole sentence
    key = fuzzy_search(" ".join(words), knowledge_base.keys())
    if key:
        return knowledge_base[key]

    # Word-by-word search
    for word in words:
        if word in knowledge_base:
            return knowledge_base[word]

    return None


def chatbot():
    bot_say("Hello! How can I assist you today? (Type 'bye' to exit)")
    start_conversation_log()

    while True:
        user = input("You: ")
        log("User: " + user)

        intent = detect_intent(user)

        if intent == "exit":
            reply = handle_intent(intent)
            bot_say(reply)
            log("Bot: " + reply)
            end_conversation_log()
            break

        if intent:
            reply = handle_intent(intent)
            bot_say(reply)
            log("Bot: " + reply)
            continue

        kb_reply = knowledge_lookup(user)
        if kb_reply:
            bot_say(kb_reply)
            log("Bot: " + kb_reply)
            continue

        fallback = "I'm not sure I understand. Could you try rephrasing?"
        bot_say(fallback)
        log("Bot: " + fallback)


if __name__ == "__main__":
    chatbot()
