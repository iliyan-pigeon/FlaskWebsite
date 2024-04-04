from flask import Flask, redirect, url_for, request

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


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usr = request.form["nm"]
        return redirect(url_for("the_user", usr=usr))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def the_user(usr):
    return f"<h1>This is the user: {usr}</h1>"


if __name__ == "__main__":
    app.run()
