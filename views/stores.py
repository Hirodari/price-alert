import json
from flask import Blueprint, render_template, url_for, request, redirect
from models.store import Store
from models.user import requires_login, requires_admin


store_blueprint = Blueprint("stores", __name__)

@store_blueprint.route("/")
@requires_login
def index():
	stores = Store.all()
	return render_template("stores/index.html", msg=stores)

@store_blueprint.route("/new", methods=["POST", "GET"])
@requires_admin
def new_store():
	if request.method == "POST":
		name = request.form['store_name']
		url_prefix = request.form['url_prefix']
		tag = request.form['tag_name']
		query = json.loads(request.form['query'])
		Store(name,url_prefix,tag,query).save_to_mongo()
		return redirect(url_for(".index"))
		# store.save_to_mongo()
	return render_template("stores/new_store.html")

@store_blueprint.route("/edit/<string:store_id>", methods=["POST","GET"])
@requires_admin
def update_store(store_id):
	store = Store.get_by_id(store_id)
	query = json.dumps(store.query)
	name = store.name.strip()
	
	if request.method == "POST":
		name = request.form['store_name']
		url_prefix = request.form['url_prefix']
		tag_name = request.form['tag_name']
		query = request.form['query']

		store.name = name
		store.url_prefix = url_prefix
		store.tag_name = tag_name
		store.query = query
		store.save_to_mongo()
		# print(name, url_prefix, tag_name, query)
		return redirect(url_for(".index"))
	return render_template("stores/update_store.html", store=store)

@store_blueprint.route("/delete/<string:store_id>")
@requires_admin
def delete(store_id):
	# store = Store.get_by_id(store_id).remove_from_mongo()
	Store.get_by_id(store_id).remove_from_mongo()
	return redirect(url_for(".index"))