from flask import Flask, render_template
import json

app = Flask(__name__)

with open("structured_output.json", "r") as f:
    questions = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
