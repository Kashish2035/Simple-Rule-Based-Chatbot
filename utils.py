from datetime import datetime
from difflib import get_close_matches
import json

LOG_FILE = "conversation_log.txt"


def start_conversation_log():
    """Start a new conversation block."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("============================================\n")
        f.write(f" Conversation started: {datetime.now()}\n")
        f.write("============================================\n")


def end_conversation_log():
    """End the current conversation block."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("============================================\n")
        f.write(f" Conversation ended: {datetime.now()}\n")
        f.write("============================================\n\n")


def log(msg):
    """Log chat messages with UTF-8 support."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")


def load_kb():
    """Load the knowledge base JSON file."""
    with open("knowledge_base.json", encoding="utf-8") as f:
        return json.load(f)


def fuzzy_search(query, kb_keys):
    """Return best matching knowledge-base key."""
    matches = get_close_matches(query, kb_keys, n=1, cutoff=0.5)
    return matches[0] if matches else None


def bot_say(text):
    """Print bot message."""
    print("🤖 Bot:", text)
