from flask import Blueprint, request, session

from dao.member_dao import MemberDao
from entity.member import Member

bp = Blueprint("api", __name__, url_prefix="/api")

memberDao = MemberDao()


@bp.route('/members')
def query_user():
    if request.args.get('username'):
        member = Member(userName=request.args.get('username'))
        result = memberDao.query_user(member)
        if result:
            return {
                'data': result
            }

    result = {
        'data': None
    }
    return result


@bp.route('/member', methods=['POST'])
def rename():
    ret = {
            "error": True
        }

    if session.get('userName', ''):
        return ret

    new_name = request.json.get('name', None)
    if new_name:
        member = Member(userName=session['userName'])
        memberDao.rename(member, new_name)

        ret = {
            "ok": True
        }

    return ret


