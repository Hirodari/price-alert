from flask import Blueprint, render_template, request, url_for, redirect, session
from models.user import User, UserError
from common.utils import Utils

user_blueprint = Blueprint("users", __name__)

@user_blueprint.route("/")
def index():
	return render_template("users/login.html")

@user_blueprint.route("/register", methods=["POST","GET"])
def register():
	if request.method == "POST":
		name = request.form['name']
		surname = request.form["surname"]
		email = request.form['email']
		password = request.form['password']
		if User.register_user(name,surname,email,password):
			session['email'] = email
			return email

		return render_template("users/register_form.html", msg="Email exists")

	return render_template("users/register_form.html")

@user_blueprint.route("/login", methods=["POST", "GET"])
def login():
	msg = None
	if request.method == "POST":
		email = request.form['email']
		password = request.form['password']
		credentials = User.login_user(email, password)
		if credentials is True:
			session['email'] = email
			return redirect(url_for("alerts.index"))

		msg = credentials if credentials else "Register"
			

	return render_template("users/login.html", msg = msg)

@user_blueprint.route("/logout", methods=["POST"])
def logout():
	print("print request method")
	print(request.method)
	if request.method == "POST":
		session['email'] = None
		print(session['email'])
		print("logout")
		return redirect(url_for(".login"))

	# return render_template("users/login.html")

