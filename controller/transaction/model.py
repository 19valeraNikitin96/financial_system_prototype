from dataclasses import dataclass


@dataclass
class TransactionJSON:
    t_type: int
    sum: int
    card_id: str
    atm_id: str
    performed_at: str
