from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/login", methods=["POST"])
def login():

    password = request.form.get("password")

    if password == "12345":
        return "To'g'ri parol"
    else:
        return "Noto'g'ri parol"

app.run(debug=True)
