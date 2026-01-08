# services/chatbot.py
from .openrouter_client import call_openrouter

def chatbot_response(message, model):
    prompt = f"User: {message}\nAssistant:"
    return call_openrouter(model, prompt)
