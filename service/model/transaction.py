from dataclasses import dataclass

from service.model import DocumentBase


class TransactionType:
    CREDIT = 1
    DEBET = 2

    @staticmethod
    def get_from_value(val: int):
        for t in TransactionType:
            if t.value == val:
                return t


@dataclass
class Transaction(DocumentBase):
    _id: str
    _type: TransactionType
    sum: int
    card_id: str
    atm_id: str
    performed_at: str

    @property
    def doc(self) -> dict:
        doc = super().doc

        del doc['_type']
        doc['type'] = self._type.value

        return doc

    def __post_init__(self):
        self._type = TransactionType.get_from_value(self._type)
