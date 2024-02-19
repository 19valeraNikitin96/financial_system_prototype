from typing import List

from controller.account import PersonJSON, AccountJSON, CardJSON
from controller.bank import ATMJSON, BankDepartmentJSON
from controller.transaction import TransactionJSON
from data_access import DBAccess
from data_access.driver.mongo import MongoCreatePayload, MongoReplicaSetImpl, MongoReadPayload, MongoUpdatePayload
from service import FinancialService
from utils import to_dict_recursive


class FinancialServiceImpl(FinancialService):

    def __init__(self, db_accesses: List[DBAccess]):
        super().__init__(db_accesses)

        self._db = MongoReplicaSetImpl(self._db_accesses)
        self._db_name = 'test'

    def register_atm(self, atm: ATMJSON) -> str:
        payload = MongoCreatePayload(self._db_name, 'atms', atm.__dict__)
        _id = self._db.create(payload)

        return _id

    def read_atm(self, _id: str) -> dict:
        payload = MongoReadPayload(self._db_name, 'atms', _id)
        data = self._db.read(payload)

        return data

    def update_atm(self, _id: str, atm: ATMJSON) -> str:
        payload = MongoUpdatePayload(self._db_name, 'atms', to_dict_recursive(atm.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def register_department(self, department: BankDepartmentJSON) -> str:
        payload = MongoCreatePayload(self._db_name, 'departments', to_dict_recursive(department.__dict__))
        _id = self._db.create(payload)

        return _id

    def update_department(self, _id: str, department: BankDepartmentJSON) -> str:
        payload = MongoUpdatePayload(self._db_name, 'departments', to_dict_recursive(department.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_department(self, _id: str) -> dict:
        payload = MongoReadPayload(self._db_name, 'departments', _id)
        data = self._db.read(payload)

        return data

    def register_person(self, person: PersonJSON) -> str:
        payload = MongoCreatePayload(self._db_name, 'persons', to_dict_recursive(person.__dict__))
        _id = self._db.create(payload)

        return _id

    def update_person(self, _id: str, person: PersonJSON):
        payload = MongoUpdatePayload(self._db_name, 'persons', to_dict_recursive(person.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_person(self, _id: str):
        payload = MongoReadPayload(self._db_name, 'persons', _id)
        data = self._db.read(payload)

        return data

    def register_card(self, card: CardJSON) -> str:
        payload = MongoCreatePayload(self._db_name, 'cards', to_dict_recursive(card.__dict__))
        _id = self._db.create(payload)

        return _id

    def update_card(self, _id: str, card: CardJSON) -> str:
        payload = MongoUpdatePayload(self._db_name, 'cards', to_dict_recursive(card.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_card(self, _id: str) -> dict:
        payload = MongoReadPayload(self._db_name, 'cards', _id)
        data = self._db.read(payload)

        return data

    def register_account(self, account: AccountJSON) -> str:
        payload = MongoCreatePayload(self._db_name, 'accounts', to_dict_recursive(account.__dict__))
        _id = self._db.create(payload)

        return _id

    def update_account(self, _id: str, account: AccountJSON) -> str:
        payload = MongoUpdatePayload(self._db_name, 'accounts', to_dict_recursive(account.__dict__), _id)
        _id = self._db.update(payload)

        return _id

    def read_account(self, _id: str) -> dict:
        payload = MongoReadPayload(self._db_name, 'accounts', _id)
        data = self._db.read(payload)

        return data

    def register_transaction(self, transaction: TransactionJSON) -> str:
        payload = MongoCreatePayload(self._db_name, 'transactions', to_dict_recursive(transaction.__dict__))
        _id = self._db.create(payload)

        return _id

    def read_transaction(self, _id: str) -> dict:
        payload = MongoReadPayload(self._db_name, 'transactions', _id)
        data = self._db.read(payload)

        return data
