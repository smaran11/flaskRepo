from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
  return '<h1 style="color: magenta">welcome to flask app</h1>'


app.run(port=4000, host="0.0.0.0", debug=True)
