from dataclasses import dataclass

from typing import List


@dataclass
class Person:
    _id: str
    firstname: str
    lastname: str
    age: int
    address: str


@dataclass
class Card:
    _id: str
    number: str
    cvv2: int
    expires_at: str


@dataclass
class Account:
    _id: str
    person_id: str
    cards_ids: List[str]
