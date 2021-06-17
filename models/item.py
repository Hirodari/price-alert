import uuid
from common.database import Database
from models.model import Model
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from typing import Dict
import requests
import re


@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    uri: str
    tag: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)


    # def __post_init__(self):
    #     self.price = None

    def page_gen(self):
        yield requests.get(self.uri).content

    def load_price(self):
        soup = BeautifulSoup(next(self.page_gen()), "html.parser")
        print(self.tag, self.query)
        price = soup.find(self.tag, self.query).get_text(strip=True)
        if len(price) > 10:
            self.price = re.findall(r'[\d]+[.,\d]+', price)[-1]
            return float(self.price)
        else:
            self.price = float(price[1:].replace(",", ""))
            return self.price

    def json(self):
        return {
            "_id": self._id,
            "uri": self.uri,
            "tag": self.tag,
            "price": self.price,
            "query": self.query
            }



