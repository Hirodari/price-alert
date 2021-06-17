from flask import Blueprint, render_template, url_for, request, redirect, session
from models.alert import Alert
from models.store import Store
from models.item import Item
from models.user import requires_login

alert_blueprint = Blueprint("alerts", __name__)

@alert_blueprint.route("/")
@requires_login
def index():
	alerts = Alert.find_many("user_email", session['email'])
	return render_template("alerts/index.html", msg=alerts)

@alert_blueprint.route("/new", methods=["POST", "GET"])
@requires_login
def new_alert():
	if request.method == "POST":
		item_url = request.form['item_url']
		alert_name = request.form['alert_name']
		price_limit = float(request.form['price_limit'])
		store = Store.find_by_url(item_url)
		item = Item(item_url, store.tag_name, store.query)
		item.load_price()
		item.save_to_mongo()
		print(session['email'])
		# print(item._id, alert_name, price_limit)
		Alert(alert_name, item._id, price_limit, session['email']).save_to_mongo()
		return redirect(url_for(".index"))
		# msg = alert.notify_if_price_reached()
	return render_template("alerts/new_alert.html")
	# return render_template("alerts/new_alerts.html", msg="No store or alert created!")


@alert_blueprint.route("/edit/<string:alert_id>", methods=["POST","GET"])
@requires_login
def update_alert(alert_id):
	alert = Alert.get_by_id(alert_id)

	if request.method == "POST":
		price_limit = float(request.form['price_limit'])
		alert.price_limit = price_limit
		alert.save_to_mongo()

		return redirect(url_for(".index"))

	return render_template("alerts/update_alert.html", alert=alert)

@alert_blueprint.route("/delete/<string:alert_id>", methods=["POST","GET"])
@requires_login
def delete(alert_id):
	alert = Alert.get_by_id(alert_id)
	# print(alert)
	if alert.user_email == session['email']:
		alert.remove_from_mongo()
		return "removed"
	return redirect(url_for(".index"))

	

