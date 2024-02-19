from dataclasses import dataclass

from typing import List

from service.model import DocumentBase


@dataclass
class Person(DocumentBase):
    _id: str
    firstname: str
    lastname: str
    age: int
    address: str


@dataclass
class Card(DocumentBase):
    _id: str
    number: str
    cvv2: int
    expires_at: str


@dataclass
class Account(DocumentBase):
    _id: str
    person_id: str
    cards: List[Card]

    def __post_init__(self):
        self.cards = [Card(**data) for data in self.cards]
