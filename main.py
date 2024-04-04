from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/template")
def template():
    return render_template("index.html")


@app.route("/single-content")
def single_content():
    return render_template("single_content.html", content="The single content!")


if __name__ == "__main__":
    app.run()
