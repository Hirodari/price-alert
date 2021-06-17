# import pymongo
from pymongo import MongoClient
from typing import Dict, Union


class Database:
    uri = "mongodb+srv://hirodaridev:parkstreet02038%40@cluster0.nxudg.mongodb.net/test?"
    client = MongoClient(uri)
    db = client.pricing

    @staticmethod
    def insert(collection, data):
        return Database.db[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.db[collection].find(query)
        
    @classmethod
    def find_one(collection, query):
        return Database.db[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        return Database.db[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.db[collection].remove(query)