from typing import List

from controller.account import PersonJSON, AccountJSON, CardJSON
from controller.bank import ATMJSON
from controller.bank.model import BankDepartmentJSON
from controller.transaction import TransactionJSON
from data_access import DBOperations, DBAccess
from service.model.account import Person, Card, Account
from service.model.bank import BankDepartment, ATM


class AccountReference:

    def __init__(self, person_id: str, cards_ids: set = None):
        self._person_id = person_id
        if cards_ids is None:
            cards_ids = set()

        self._cards_ids = cards_ids

    def add_card_id(self, card_id: str):
        self._cards_ids.add(card_id)


class BankDepartmentsReference:

    def __init__(self, atms_ids: set = None):
        if atms_ids is None:
            atms_ids = set()

        self._atms_ids = atms_ids

    def add_atm_id(self, atm_id: str):
        self._atms_ids.add(atm_id)


class CardTransactionsReference:

    def __init__(self):
        self._storage = dict()

    def put_transaction(self, card_id: str, transaction_id: str):
        if card_id not in self._storage.keys():
            self._storage[card_id] = set()

        self._storage[card_id].add(transaction_id)


class FinancialService:

    def __init__(self):
        self._transactions_by_accounts = dict()
        self._bank_departments = dict()
        self._accounts_references = dict()

        self._account_by_card = dict()

    def put_account_id_by_card_id(self, card_id: str, account_id: str):
        self._account_by_card[card_id] = account_id

    def put_atm_ref_to_department(self, department_id: str, atm_id: str):
        if department_id not in self._bank_departments.keys():
            self._bank_departments[department_id] = BankDepartmentsReference()

        refs: BankDepartmentsReference = self._bank_departments[department_id]
        refs.add_atm_id(atm_id)

    def put_card_id_to_account(self, account_id: str, person_id: str, card_ids: set = None):
        if account_id in self._accounts_references.keys():
            raise Exception()

        if card_ids is None:
            card_ids = set()

        self._accounts_references[account_id] = AccountReference(person_id, card_ids)

    def add_card_id_to_account(self, account_id: str, card_id: str):
        if account_id not in self._accounts_references.keys():
            raise Exception()

        refs: AccountReference = self._accounts_references[account_id]
        refs.add_card_id(card_id)

    def add_transaction_by_card(self, account_id: str, card_id: str, transaction_id: str):
        if account_id not in self._transactions_by_accounts.keys():
            self._transactions_by_accounts[account_id] = CardTransactionsReference()

        refs: CardTransactionsReference = self._transactions_by_accounts[account_id]
        refs.put_transaction(card_id, transaction_id)

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

    def register_person(self, person: PersonJSON) -> str: ...

    def update_person(self, _id: str, person: PersonJSON) -> str: ...

    def read_person(self, _id: str) -> dict: ...

    def register_card(self, card: CardJSON) -> str: ...

    def update_card(self, _id: str, card: CardJSON) -> str: ...

    def read_card(self, _id: str) -> dict: ...

    def register_account(self, account: AccountJSON) -> str: ...

    def update_account(self, _id: str, account: AccountJSON) -> str: ...

    def read_account(self, _id: str) -> dict: ...

    def register_transaction(self, transaction: TransactionJSON) -> str: ...

    def read_transaction(self, _id: str) -> dict: ...
