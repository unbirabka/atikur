"""Testing Code Rukita"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Testing Code Rukita"""
    return "Congratulations, it's service-a"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
