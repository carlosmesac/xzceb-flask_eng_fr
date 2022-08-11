from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation import translator
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate)
    # Write your code here
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate)
    # Write your code here
    return translated_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8080)
