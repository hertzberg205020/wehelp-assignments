from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session


app = Flask(__name__,
            static_folder="static",
            static_url_path="/static")

app.secret_key = "myPassWordIsWeak@109"


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def sign_in():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        session['account'] = account
        session['password'] = password
        return redirect("/member/")

    return redirect("/error/?message=帳號或密碼輸入錯誤")


@app.route("/member/")
def member():
    if session.get("account", "") and session.get("password", ""):
        return render_template("successfully_login.html")
    return redirect("/")


@app.route("/error/")
def handle_error():
    error_msg = request.args.get("message", "")
    return render_template("fail_login.html", info=error_msg)


@app.route("/signout/")
def sign_out():
    session['account'] = None
    session['password'] = None
    return redirect("/")


if __name__ == '__main__':
    app.run(port=3000)
