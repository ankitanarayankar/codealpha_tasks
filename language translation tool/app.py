from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    src_lang = ""
    dest_lang = ""
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        src_lang = request.form["src_lang"]
        dest_lang = request.form["dest_lang"]

        if text.strip():
            translated = translator.translate(text, src=src_lang, dest=dest_lang)
            translated_text = translated.text

    return render_template("index.html", 
                           languages=LANGUAGES, 
                           translated_text=translated_text,
                           text=text, 
                           src_lang=src_lang, 
                           dest_lang=dest_lang)

if __name__ == "__main__":
    app.run(debug=True)



