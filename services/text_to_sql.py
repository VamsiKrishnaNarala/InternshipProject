# services/text_to_sql.py
from .openrouter_client import call_openrouter

def text_to_sql(question, schema, model):
    prompt = f"""
Convert the following natural language question into SQL.

Schema:
{schema}

Question:
{question}

Return ONLY SQL.
"""
    return call_openrouter(model, prompt)
