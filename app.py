import random
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

QUOTES = [
    {"text": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
    {"text": "Small steps every day add up to big changes.", "author": "Anonymous"},
    {"text": "You don't have to be perfect to make progress.", "author": "Unknown"},
    {"text": "Today is a good day to begin again.", "author": "Marcus Aurelius"},
    {"text": "Difficult roads often lead to beautiful places.", "author": "Zig Ziglar"},
    {"text": "Focus on getting a little better each day.", "author": "James Clear"},
    {"text": "Mistakes are proof that you are trying.", "author": "Jennifer Lim"},
    {"text": "Your effort today is building your tomorrow.", "author": "Ken Poirot"},
    {"text": "Don't wait for motivation. Start, and it will follow.", "author": "Jerome Bruner"},
    {"text": "Every expert was once a beginner.", "author": "Helen Hayes"},
    {"text": "Be patient with yourself. Growth takes time.", "author": "David Foster Wallace"},
    {"text": "One finished page is better than ten perfect plans.", "author": "Austin Kleon"},
    {"text": "Courage is taking the next step, even when you are unsure.", "author": "Mary Anne Radmacher"},
    {"text": "Keep going. You are closer than you think.", "author": "Confucius"},
    {"text": "A calm mind solves problems that a rushed one cannot.", "author": "Thich Nhat Hanh"},
]

last_quote = None


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/quote")
def get_quote():
    """Return a random quote, avoiding an immediate repeat."""
    global last_quote
    choices = [q for q in QUOTES if q != last_quote]
    last_quote = random.choice(choices)
    return jsonify({"quote": last_quote["text"], "author": last_quote["author"]})


if __name__ == "__main__":
    app.run(debug=True)
