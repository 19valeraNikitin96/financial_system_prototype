from dataclasses import dataclass

from typing import List


@dataclass
class PersonJSON:
    firstname: str
    lastname: str
    birthday: str
    address: str


@dataclass
class CardJSON:
    number: str
    cvv2: int
    expires_at: str
    balance: int


@dataclass
class AccountJSON:
    person_id: str
    cards_ids: List[str]
    active: bool
