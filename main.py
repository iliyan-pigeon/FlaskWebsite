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


@app.route("/list-of-contents")
def list_of_contents():
    return render_template("list_of_contents.html", content=["first", "second", "third"])


if __name__ == "__main__":
    app.run()
