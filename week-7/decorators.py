from functools import wraps

from flask import redirect,session


def login_required(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        if session.get('userName', ''):
            return func(*args, **kwargs)
        return redirect('/')

    return inner_func
