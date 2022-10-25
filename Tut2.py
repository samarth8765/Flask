from flask import Flask, redirect , url_for, render_template

#instanc of flask app
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html",content=['a','b','c','d'])


if __name__ == '__main__':
    app.run()