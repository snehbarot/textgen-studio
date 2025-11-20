from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a small text-generation model (fast & lightweight)
generator = pipeline("text-generation", model="distilgpt2")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt.strip():
        return jsonify({"error": "Prompt cannot be empty"}), 400

    # Generate text
    output = generator(prompt, max_length=100, num_return_sequences=1)

    return jsonify({"result": output[0]["generated_text"]})

if __name__ == "__main__":
    app.run(debug=True)

