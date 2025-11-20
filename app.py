from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# A simple mock AI generator (not using any paid API)
def generate_text(prompt):
    responses = [
        f"Here is an idea related to '{prompt}': Always keep it simple and structured.",
        f"For the topic '{prompt}', you can focus on real-world examples.",
        f"The concept '{prompt}' can be explained better using a story.",
        f"My thoughts on '{prompt}': break it down into smaller steps."
    ]
    return random.choice(responses)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    result = generate_text(prompt)
    return jsonify({"output": result})

if __name__ == '__main__':
    app.run(debug=True)
