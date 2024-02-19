from dataclasses import dataclass


class TransactionType:
    CREDIT = 1
    DEBET = 2


@dataclass
class Transaction:
    _type: TransactionType
    sum: int
    card_id: str
    atm_id: str
    performed_at: str
