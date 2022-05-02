import csv
from flask import Flask, jsonify, request
app = Flask(__name__)

with open('top10movies.csv', newline="") as f:
  reader = csv.reader(f)
  movies_data = list(reader)
 


@app.route("/")
def index():
    return jsonify({
        "data": movies_data,
        "message": "success"
    }), 200





if __name__ == "__main__":
    app.run()
