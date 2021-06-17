from dataclasses import dataclass, field
from models.model import Model
from common.utils import Utils
from models.user import UserError
import uuid 


@dataclass
class User(Model):
	collection: str = field(init = False, default="user")
	name: str 
	surname: str
	email: str
	password: str 
	_id: str = field(default_factory = lambda: uuid.uuid4().hex)

	@classmethod
	def find_by_email(cls, email: str) -> "User":
		try:
			return cls.find_one("email", email)
		except TypeError:
			return False

	@classmethod
	def register_user(cls, name: str, surname: str, email: str, password: str) -> bool:
		if not Utils.email_is_valid(email):
			return "The e-mail does not have the right format"

		if cls.find_by_email(email):
				return False

		User(name,surname,email,Utils.hash_password(password)).save_to_mongo()
		return True 

	@classmethod
	def login_user(cls, email: str, password: str) -> bool:
		if Utils.email_is_valid(email):
			credentials = cls.find_by_email(email)
			if credentials:
				if Utils.check_hashed_password(password, credentials.password) and email == credentials.email:
					return True
				return "Wrong password"
			return "register"
		return "incorrect email"



			

	def json(self):
		return {
			"_id": self._id,
			"name": self.name,
			"surname": self.surname,
			"email": self.email,
			"password": self.password
		}