class UserError(Exception):
	def __init__(self,message):
		self.message = message

	def UserNotFoundError(UserError):
		pass

	def InvalidEmailError(UserError):
		pass 

	def UserAlreadyRegisteredError(UserError):
		pass
