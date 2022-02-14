from flask import Blueprint, render_template, request, redirect, url_for, session

from dao.member_dao import MemberDao
from decorators import login_required
from entity.member import Member

bp = Blueprint("user", __name__, url_prefix="/")

memberDao = MemberDao()


@bp.route('/')
def index():
    return render_template("index.html")


@bp.route('/register', methods=['POST'])
def register():
    name = request.form["name"]
    userName = request.form["userName"]
    password = request.form["password"]
    if name and userName and password:
        member = Member(None, name, userName, password)
        if memberDao.is_valid_create_account(member):
            memberDao.insert(member)
            return redirect(url_for('user.index'))
        else:
            return redirect("/error/?message=帳號已被註冊")

    return redirect("/error/?message=姓名, 帳號, 密碼全部要填寫")


@bp.route("/signin", methods=["POST"])
def sign_in():
    userName = request.form["userName"]
    password = request.form["password"]

    if userName == "" or password == "":
        return redirect("/error/?message=請輸入帳號, 密碼")

    member = Member(None, None, userName, password)
    if memberDao.is_valid(member):
        session['userName'] = userName
        return redirect("/member/")

    return redirect("/error/?message=帳號或密碼輸入錯誤")


@bp.route("/member/")
@login_required
def evaluate_member():
    name = memberDao.query_user(Member(userName=session.get("userName", ""))).get('name', '')
    return render_template("successfully_login.html", info=name)


@bp.route("/error/")
def handle_error():
    error_msg = request.args.get("message", "")
    return render_template("fail_login.html", info=error_msg)


@bp.route("/signout/")
def sign_out():
    session.clear()
    return redirect("/")

