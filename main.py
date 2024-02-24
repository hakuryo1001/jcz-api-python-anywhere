from flask import Flask, request, jsonify
from firebase_functions import https_fn

from flask_cors import CORS
from jcz import transliterate

import os


app = Flask(__name__)
CORS(app)


# Rest of your Flask app code...

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/dumb-jcz")
def translate_text():
    translated_text = transliterate.pipe_transliterator(
        "咁都係果啲嘢㗎啦，廿鯪蚊個餐又湯又剩唔通有得你食天九翅咩？求求其其有啲肉有啲菜蛋白質澱粉質撈撈埋埋打個白汁茄汁黑椒汁咁撐得你懵口懵面咪纍返去返工返學返廠返寫字樓囉。唔係你估真係搵餐晏仔咁簡單啊。咁跟飯定跟意粉啊？"
    )
    return f"<p>{translated_text}</p>"  # This will be displayed with font.
    #  return jsonify({"translatedText": translated_text}) # This will be displayed as gibberish code


@app.route("/translate", methods=["POST"])
def translate_jcz():
    text_to_translate = request.json.get("text")
    translated_text = transliterate.pipe_transliterator(text_to_translate)
    return jsonify({"translatedText": translated_text})


# curl -X POST http://localhost:5000/translate \
# -H "Content-Type: application/json" \
# -d '{"text": "咁都係果啲嘢㗎啦，廿鯪蚊個餐又湯又剩唔通有得你食天九翅咩？求求其其有啲肉有啲菜蛋白質澱粉質撈撈埋埋打個白汁茄汁黑椒汁咁撐得你懵口懵面咪纍返去返工返學返廠返寫字樓囉。唔係你估真係搵餐晏仔咁簡單啊。咁跟飯定跟意粉啊？"}'


@app.route("/instantChoicefulTranslate", methods=["POST"])
def instantChoicefulTranslate():
    data = request.json
    text_to_translate = data.get("text")
    mode = data.get("mode", "font")
    orthography = data.get("orthography", "jcz_only")
    use_repeat_char = data.get("useRepeatChar", True)
    initial_r_block = data.get("initialRBlock", "wl")
    v_block = data.get("vBlock", "f")
    use_schwa_char = data.get("useSchwaChar", True)
    tone_config = data.get("toneConfig", "vertical")
    print(
        data,
        text_to_translate,
        mode,
        orthography,
        use_repeat_char,
        initial_r_block,
        v_block,
        use_schwa_char,
        tone_config,
    )
    translated_text = transliterate.pipe_transliterator(
        text_to_translate,
        mode=mode,
        orthography=orthography,
        use_repeat_char=use_repeat_char,
        initial_r_block=initial_r_block,
        v_block=v_block,
        use_schwa_char=use_schwa_char,
        tone_config=tone_config,
    )
    return jsonify({"translatedText": translated_text})


@app.route("/echo", methods=["POST"])
def echo_data():
    data = request.get_json()
    if not data:
        return {"error": "No data provided"}, 400
    return jsonify(data), 200


# if __name__ == "__main__":
#     app.run()


# curl -X POST http://localhost:3000/api/echo -H "Content-Type: application/json" -d '{"key": "value"}'

# curl -X POST http://localhost:5000/api/echo -H "Content-Type: application/json" -d '{"key": "value"}'
