from typing import List

from controller.bank import ATMJSON, BankDepartmentJSON
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

    # def register_bank_department(self, department: BankDepartment):
    #     atms = department.atms
    #
    #     for atm in atms:
    #         if atm.id is None:
    #             data = atm.doc
    #             create = MongoCreatePayload(self._db_name, 'atms', data)
    #             _id = self._db_access.create(create)
    #
    #
    # def get_bank_department(self):
    #     pass
    #
    # def register_account(self):
    #     pass
    #
    # def update_account(self):
    #     pass
    #
    # def get_account(self):
    #     pass
    #
    # def add_credit_card(self):
    #     pass
    #
    # def register_atm(self, atm: ATMJSON):
    #     pass
    #
    # def save_transaction(self):
    #     pass
