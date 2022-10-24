from flask import Flask, redirect , url_for

#instanc of flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"
@app.route("/<name>")
def users(name):
    return f"Hello {name} !"

@app.route('/admin')
def admin():
    redirect(url_for("home"))

if __name__ == '__main__':
    app.run()