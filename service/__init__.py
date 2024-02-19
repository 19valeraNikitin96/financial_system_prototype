from typing import List

from controller.bank import ATMJSON
from controller.bank.model import BankDepartmentJSON
from data_access import DBOperations, DBAccess
from service.model.account import Person, Card, Account
from service.model.bank import BankDepartment, ATM


class BankDepartmentsReferenceStorage:

    def __init__(self):
        self._storage = dict()

    def put(self, department: BankDepartment):
        if department.id is None:
            raise Exception('Department ID must be not None')

        atms_refs = {atm.id for atm in department.atms}
        if None in atms_refs:
            raise Exception('ATM ID must not be None')

        refs = {
            'atms': atms_refs
        }
        self._storage[department.id] = refs

    def add_atm_ref(self, department_id: str, atm_id: str):
        if None in [department_id, atm_id]:
            raise Exception('Must be not None')

        self._storage[department_id]['atms'].add(atm_id)

    def get(self, department_id: str) -> dict:
        return self._storage[department_id]


class AccountReferenceStorage:

    def __init__(self):
        self._storage = dict()

    def put(self, acc: Account):
        if acc.id is None:
            raise Exception('Account ID must be not None')

        if acc.person_id is None:
            raise Exception('ATM ID must not be None')

        card_ids = [card.id for card in acc.cards]
        if None in card_ids:
            raise Exception()

        refs = {
            'person_id': acc.person_id,
            'cards_ids': card_ids
        }
        self._storage[acc.id] = refs

    def get(self, account_id: str) -> dict:
        return self._storage[account_id]


class FinancialService:

    def __init__(self, db_accesses: List[DBAccess]):
        self._db_accesses = db_accesses

        self._bank_departments = BankDepartmentsReferenceStorage()
        self._atms = dict()

        self._persons = dict()
        self._accounts = AccountReferenceStorage()
        self._cards = dict()

    # def put_bank_department(self, _id: str, department: BankDepartment):
    #     self._bank_departments[_id] = department
    #
    # def put_atm(self, _id: str, atm: ATM):
    #     self._atms[_id] = atm
    #
    # def put_person(self, _id: str, person: Person):
    #     self._persons[_id] = person
    #
    # def put_card(self, _id: str, card: Card):
    #     self._cards[_id] = card
    #
    # def put_account(self, _id: str, acc: Account):
    #     self._accounts[_id] = acc

    def register_atm(self, atm: ATMJSON) -> str: ...

    def read_atm(self, _id: str) -> dict: ...

    def update_atm(self, _id: str, atm: ATMJSON) -> str: ...

    def register_department(self, department: BankDepartmentJSON) -> str: ...

    def update_department(self, _id: str, department: BankDepartmentJSON) -> str: ...

    def read_department(self, _id: str) -> dict: ...

    # def register_bank_department(self, department: BankDepartmentJSON): ...
    #
    # def get_bank_department(self): ...
    #
    # def register_account(self): ...
    #
    # def update_account(self): ...
    #
    # def get_account(self): ...
    #
    # def add_credit_card(self): ...
    #
    # def save_transaction(self): ...
