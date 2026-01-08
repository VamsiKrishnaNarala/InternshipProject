# services/summarization.py
from .openrouter_client import call_openrouter

def summarize(text, model):
    prompt = f"Summarize the following text clearly and concisely:\n{text}"
    return call_openrouter(model, prompt)
