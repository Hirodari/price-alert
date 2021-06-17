import re 
from passlib.hash import pbkdf2_sha512


class Utils:
	@staticmethod
	def email_is_valid(email: str) -> bool: 
		email_matcher = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
		return True if re.search(email_matcher,email) else False

	@staticmethod
	def hash_password(password: str) -> str:
		return pbkdf2_sha512.encrypt(password)

	@staticmethod
	def check_hashed_password(password: str, hash_password: str) -> bool:
		return pbkdf2_sha512.verify(password, hash_password)

	