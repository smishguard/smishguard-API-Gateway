from flask import Flask, jsonify

app = Flask(__name__)
application = app

@app.route('/')
def hello_world():
    return 'hello, world!'

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})


if __name__ == '__main__':
    app.run(debug = True)
