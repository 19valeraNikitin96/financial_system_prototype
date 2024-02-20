import logging
import os

from controller.account import PersonJSON, AccountJSON, CardJSON
from controller.bank import ATMJSON, BankDepartmentJSON
from controller.transaction import TransactionJSON
from data_access import DBAccess, DBCreatePayload, DBReadPayload, DBUpdatePayload
from data_access.driver.autumn_db.impl import AutumnDBImpl
from service import FinancialService
from utils import to_dict_recursive


class FinancialServiceImpl(FinancialService):

    def __init__(self):
        super().__init__()

        db_addr = os.environ['DB_ADDR']
        db_port = os.environ['DB_PORT']
        access = DBAccess(db_addr, int(db_port))

        self._db = AutumnDBImpl(access)

    def register_atm(self, atm: ATMJSON) -> str:
        payload = DBCreatePayload('atms', to_dict_recursive(atm.__dict__))
        _id = self._db.create(payload)

        return _id

    def read_atm(self, _id: str) -> dict:
        payload = DBReadPayload('atms', _id)
        data = self._db.read(payload)

        return data

    def update_atm(self, _id: str, atm: ATMJSON) -> str:
        payload = DBUpdatePayload('atms', to_dict_recursive(atm.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def register_department(self, department: BankDepartmentJSON) -> str:
        payload = DBCreatePayload('departments', to_dict_recursive(department.__dict__))
        _id = self._db.create(payload)

        for atm_id in department.atms_ids:
            self.put_atm_ref_to_department(_id, atm_id)

        return _id

    def update_department(self, _id: str, department: BankDepartmentJSON) -> str:
        payload = DBUpdatePayload('departments', to_dict_recursive(department.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_department(self, _id: str) -> dict:
        payload = DBReadPayload('departments', _id)
        data = self._db.read(payload)

        return data

    def register_person(self, person: PersonJSON) -> str:
        payload = DBCreatePayload('persons', to_dict_recursive(person.__dict__))
        _id = self._db.create(payload)

        return _id

    def update_person(self, _id: str, person: PersonJSON):
        payload = DBUpdatePayload('persons', to_dict_recursive(person.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_person(self, _id: str):
        payload = DBReadPayload('persons', _id)
        data = self._db.read(payload)

        return data

    def register_card(self, card: CardJSON) -> str:
        payload = DBCreatePayload('cards', to_dict_recursive(card.__dict__))
        _id = self._db.create(payload)

        return _id

    def update_card(self, _id: str, card: CardJSON) -> str:
        payload = DBUpdatePayload('cards', to_dict_recursive(card.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_card(self, _id: str) -> dict:
        payload = DBReadPayload('cards', _id)
        data = self._db.read(payload)

        return data

    def register_account(self, account: AccountJSON) -> str:
        payload = DBCreatePayload('accounts', to_dict_recursive(account.__dict__))
        _id = self._db.create(payload)

        cards_ids = set(account.cards_ids)
        self.put_card_id_to_account(_id, account.person_id, cards_ids)

        for card_id in cards_ids:
            self.put_account_id_by_card_id(card_id, _id)

        return _id

    def update_account(self, _id: str, account: AccountJSON) -> str:
        payload = DBUpdatePayload('accounts', to_dict_recursive(account.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_account(self, _id: str) -> dict:
        payload = DBReadPayload('accounts', _id)
        data = self._db.read(payload)

        return data

    def register_transaction(self, transaction: TransactionJSON) -> str:
        payload = DBCreatePayload('transactions', to_dict_recursive(transaction.__dict__))
        _id = self._db.create(payload)

        account_id = self._account_by_card[transaction.card_id]
        self.add_transaction_by_card(account_id, transaction.card_id, _id)

        payload = DBReadPayload('cards', transaction.card_id)
        data = self._db.read(payload)

        balance = data['balance']
        sum = transaction.sum
        if transaction.t_type == 1:
            sum *= -1

        balance += sum
        data['balance'] = balance
        logging.debug(f"Balance: {balance}, card ID: {transaction.card_id}")

        payload = DBUpdatePayload('cards', data, transaction.card_id)
        _id = self._db.update(payload)

        return _id

    def read_transaction(self, _id: str) -> dict:
        payload = DBReadPayload('transactions', _id)
        data = self._db.read(payload)

        return data
