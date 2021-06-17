from  abc import ABCMeta, abstractmethod
from common.database import Database
from typing import Dict, Union

class Model(metaclass=ABCMeta):

	@abstractmethod
	def json(self):
		raise NotImplementedError


	@classmethod
	def all(cls):
		return [cls(**item) for item in Database.find(cls.collection, {})]

	
	def save_to_mongo(self):
		return Database.update(self.collection, {"_id": self._id},	self.json())

	
	def remove_from_mongo(self):
		return Database.remove(self.collection, {"_id": self._id}, self.json())

	@classmethod
	def find_one(cls, attribute: str, value: Union[str, Dict]):
		# print(attribute, value, cls.collection)
		return cls(**Database.db[cls.collection].find_one({attribute: value}))

	# def find_one(collection, query):
 #        return Database.db[collection].find_one(query)
		

	@classmethod
	def find_many(cls, attribute, value):
		return [cls(**element) for element in Database.find(cls.collection, {attribute: value})]

	@classmethod
	def get_by_id(cls, id):
		return cls.find_one("_id", id)