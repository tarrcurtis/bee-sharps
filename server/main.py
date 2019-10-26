from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
