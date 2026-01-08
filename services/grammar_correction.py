from .openrouter_client import call_openrouter

def grammar_correct(text, model):
    prompt = f"""
Correct the grammar and spelling of the following text.
Return only the corrected text.

Text:
{text}
"""
    return call_openrouter(model, prompt)
