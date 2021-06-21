__author__ = "Fred B"
from views.items import item_blueprint
from views.alerts import alert_blueprint
from views.items import item_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from models.store import Store
from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(64)
'''
app.config set permission to admin for certain task
in this app is for store ressources
pip install python-dotenv for env to be visible 
'''
@app.route('/')
def home():
	return render_template("home.html")
	
app.config.update(
	ADMIN = os.environ.get('ADMIN')
	)
	
app.register_blueprint(item_blueprint, url_prefix="/items")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)


	

