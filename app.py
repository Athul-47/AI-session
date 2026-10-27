import random
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

QUOTES = [
    "Start where you are. Use what you have. Do what you can.",
    "Small steps every day add up to big changes.",
    "You don't have to be perfect to make progress.",
    "Today is a good day to begin again.",
    "Difficult roads often lead to beautiful places.",
    "Focus on getting a little better each day.",
    "Mistakes are proof that you are trying.",
    "Your effort today is building your tomorrow.",
    "Don't wait for motivation. Start, and it will follow.",
    "Every expert was once a beginner.",
    "Be patient with yourself. Growth takes time.",
    "One finished page is better than ten perfect plans.",
    "Courage is taking the next step, even when you are unsure.",
    "Keep going. You are closer than you think.",
    "A calm mind solves problems that a rushed one cannot.",
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
    return jsonify({"quote": last_quote})


if __name__ == "__main__":
    app.run(debug=True)
