import hashlib

from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from dao.member_dao import MemberDao
from entity.member import Member

app = Flask(__name__,
            static_folder="static",
            static_url_path="/static")

app.secret_key = hashlib.sha256(b"123456").hexdigest()
memberDao = MemberDao()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    name = request.form["name"]
    userName = request.form["userName"]
    password = request.form["password"]
    member = Member(name, userName, password)
    if memberDao.is_valid_create_account(member):
        memberDao.insert(member)
        return redirect(url_for('index'))
    else:
        return redirect("/error/?message=帳號已被註冊")


@app.route("/signin", methods=["POST"])
def sign_in():
    userName = request.form["userName"]
    password = request.form["password"]

    if userName == "" or password == "":
        return redirect("/error/?message=請輸入帳號, 密碼")

    member = Member(None, userName, password)
    if memberDao.is_valid(member):
        session['userName'] = userName
        session['password'] = password
        return redirect("/member/")

    return redirect("/error/?message=帳號或密碼輸入錯誤")


@app.route("/member/")
def evaluate_member():
    if session.get("userName", "") and session.get("password", ""):
        return render_template("successfully_login.html", info=session.get("userName", ""))
    return redirect("/")


@app.route("/error/")
def handle_error():
    error_msg = request.args.get("message", "")
    return render_template("fail_login.html", info=error_msg)


@app.route("/signout/")
def sign_out():
    session['userName'] = None
    session['password'] = None
    return redirect("/")


if __name__ == '__main__':
    app.run(port=3000)

