from .openrouter_client import call_openrouter

def paraphrase(text, model):
    prompt = f"""
Rewrite the following text without changing its meaning.
Use simple and clear language.

Text:
{text}
"""
    return call_openrouter(model, prompt)
