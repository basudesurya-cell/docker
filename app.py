from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO DOCKER...!!! DOCKER IS RUNNING ON SERVER"

@app.route("/about")
def about():
    return "This is my first program in Docker class"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)