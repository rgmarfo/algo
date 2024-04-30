from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pages/index.html")

@app.route("/feedback", methods=['GET'])
def bisection():
    return render_template("pages/feedback.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)