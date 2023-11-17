from flask import Flask, jsonify, request
from flask_cors import CORS
from ebay import run

app = Flask(__name__)
CORS(app)

# Access this endpoint through: http://localhost:5000/
@app.route('/get/<query>')
def index(query):
    # print(query)
    print("hey someone is here")
    response = run(query)
    return jsonify(response)
    # return jsonify({"hi": "fghjk"})


@app.route('/')
def home():
    return jsonify({"hi": "fghjk"})


@app.route('/abc')
def sdf():
    return jsonify({"hi": "abc"})