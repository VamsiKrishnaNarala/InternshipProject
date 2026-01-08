# services/translation.py
from .openrouter_client import call_openrouter

def translate(text, language, model):
    prompt = f"""
Translate the following text into {language}.
Only return the translated text.

Text:
{text}
"""
    return call_openrouter(model, prompt)

