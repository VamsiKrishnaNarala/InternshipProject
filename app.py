from flask import Flask, render_template, request
import os
from flask import session
from services.openrouter_client import call_openrouter
from services.summarization import summarize
from services.translation import translate
from services.chatbot import chatbot_response
from services.text_to_sql import text_to_sql
from services.paraphrasing import paraphrase
from services.grammar_correction import grammar_correct

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    audio_file = None

    if request.method == "POST":
        task = request.form["task"]
        model = request.form["model"]

        if task == "summarization":
            text = request.form.get("summary_text", "")
            output = summarize(text, model)

        elif task == "translation":
            text = request.form.get("translation_text", "")
            language = request.form.get("language", "")
            output = translate(text, language, model)

        elif task == "chatbot":
            text = request.form.get("chat_text", "")
            output = chatbot_response(text, model)

        elif task == "text_to_sql":
            question = request.form.get("sql_question", "")
            schema = request.form.get("schema", "")
            output = text_to_sql(question, schema, model)

        elif task == "paraphrasing":
            text = request.form.get("paraphrase_text", "")
            output = paraphrase(text, model)

        elif task == "grammar":
            text = request.form.get("grammar_text", "")
            output = grammar_correct(text, model)

    return render_template("index.html", output=output, audio_file=audio_file)

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot_ui():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_msg = request.form.get("chat_input", "")
        model = request.form.get("model")

        if user_msg:
            # Add user message
            session["chat_history"].append(
                {"role": "user", "content": user_msg}
            )

            # Build prompt from history
            prompt = ""
            for msg in session["chat_history"]:
                prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"

            # Call LLM
            bot_reply = call_openrouter(model, prompt)

            # Add bot reply
            session["chat_history"].append(
                {"role": "assistant", "content": bot_reply}
            )

            session.modified = True

    return render_template(
        "chatbot.html",
        chat_history=session["chat_history"]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

