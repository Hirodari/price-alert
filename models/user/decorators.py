import functools
from typing import Callable
from flask import flash, session, url_for, redirect, current_app


def requires_login(f: Callable)-> Callable:
	@functools.wraps(f)
	def decorated_function(*args, **kwargs):
		if not session.get("email"):
			flash("you need to sign in for this page", "danger")
			return redirect(url_for("users.login"))
		return f(*args, **kwargs)
	return decorated_function

def requires_admin(f: Callable)-> Callable:
	@functools.wraps(f)
	def decorated_function(*args, **kwargs):
		if session.get("email") != current_app.config.get('ADMIN', ''):
			flash("You need to be an admin to access this page",  "danger")
			return redirect(url_for("users.login"))
		return f(*args, **kwargs)
	return decorated_function
