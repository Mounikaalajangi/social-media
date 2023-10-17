from flask import Flask, render_template, request

app = Flask(__name__) # initializing flask app

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = False, port = 8000)
