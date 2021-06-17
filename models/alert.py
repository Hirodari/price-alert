import uuid
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model
from models.user import User
from common.database import Database
from libs.mailgun import Mailgun


@dataclass(eq=False)
class Alert(Model):
	collection: str = field(init=False, default="alert")
	name: str
	item_id: str
	price_limit: float
	user_email: str
	price: float = field(default="alert")
	_id: str = field(default_factory=lambda: uuid.uuid4().hex)


	def __post_init__(self):
		self.item = Item.get_by_id(self.item_id)
		self.user = User.find_by_email(self.user_email)

	def json(self):
		
		return {
			"_id": self._id,
			"name": self.name,
			"price": self.item.load_price(),
			"price_limit": self.price_limit,
			"user_email": self.user_email,
			"item_id": self.item_id
		}


	def load_item_price(self):
		return self.item.load_price()



	def notify_if_price_reached(self):
		if self.load_item_price() < self.price_limit:
			# return f"Item has reached a price under {self.price_limit} latest price {self.item.load_price()}"
			message = f"Item has reached a price under {self.price_limit} latest price {self.item.load_price()}"
			return Mailgun(message).send_simple_message()
