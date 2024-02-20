import json

import requests

from controller.account import PersonJSON, CardJSON, AccountJSON
from controller.bank import ATMJSON, BankDepartmentJSON
from controller.transaction import TransactionJSON
from utils import to_dict_recursive

# addr = '127.0.0.1'
# port = 6001
url_prefix = 'http://127.0.0.1:6001/'

### PERSON
def create_person(person: PersonJSON) -> str:
    data = to_dict_recursive(person.__dict__)
    payload = json.dumps(data)

    resp = requests.post(f"{url_prefix}persons", data=payload).json()

    return resp['id']


def update_person(_id: str, person: PersonJSON) -> str:
    data = to_dict_recursive(person.__dict__)
    payload = json.dumps(data)

    headers = {
        'Id': _id
    }
    resp = requests.put(f"{url_prefix}persons", headers=headers, data=payload).json()

    return resp['id']


def read_person(_id: str) -> dict:
    headers = {
        'Id': _id
    }
    resp = requests.get(f"{url_prefix}persons", headers=headers).json()

    return resp


### CARD


def create_card(card: CardJSON) -> str:
    data = to_dict_recursive(card.__dict__)
    payload = json.dumps(data)

    resp = requests.post(f"{url_prefix}cards", data=payload).json()

    return resp['id']


def update_card(_id: str, card: CardJSON) -> str:
    data = to_dict_recursive(card.__dict__)
    payload = json.dumps(data)

    headers = {
        'Id': _id
    }
    resp = requests.put(f"{url_prefix}cards", headers=headers, data=payload).json()

    return resp['id']


def read_card(_id: str) -> dict:
    headers = {
        'Id': _id
    }
    resp = requests.get(f"{url_prefix}cards", headers=headers).json()

    return resp


### ACCOUNT


def create_account(account: AccountJSON) -> str:
    data = to_dict_recursive(account.__dict__)
    payload = json.dumps(data)

    resp = requests.post(f"{url_prefix}accounts", data=payload).json()

    return resp['id']


def update_account(_id: str, account: PersonJSON) -> str:
    data = to_dict_recursive(account.__dict__)
    payload = json.dumps(data)

    headers = {
        'Id': _id
    }
    resp = requests.put(f"{url_prefix}accounts", headers=headers, data=payload).json()

    return resp['id']


def read_account(_id: str) -> dict:
    headers = {
        'Id': _id
    }
    resp = requests.get(f"{url_prefix}accounts", headers=headers).json()

    return resp

### ATM


def create_atm(atm: ATMJSON) -> str:
    data = to_dict_recursive(atm.__dict__)
    payload = json.dumps(data)

    resp = requests.post(f"{url_prefix}atms", data=payload).json()

    return resp['id']


def update_atm(_id: str, atm: ATMJSON) -> str:
    data = to_dict_recursive(atm.__dict__)
    payload = json.dumps(data)

    headers = {
        'Id': _id
    }
    resp = requests.put(f"{url_prefix}atms", headers=headers, data=payload).json()

    return resp['id']


def read_atm(_id: str) -> dict:
    headers = {
        'Id': _id
    }
    resp = requests.get(f"{url_prefix}atms", headers=headers).json()

    return resp

### BANK DEPARTMENT


def create_department(department: BankDepartmentJSON) -> str:
    data = to_dict_recursive(department.__dict__)
    payload = json.dumps(data)

    resp = requests.post(f"{url_prefix}departments", data=payload).json()

    return resp['id']


def update_department(_id: str, department: BankDepartmentJSON) -> str:
    data = to_dict_recursive(department.__dict__)
    payload = json.dumps(data)

    headers = {
        'Id': _id
    }
    resp = requests.put(f"{url_prefix}departments", headers=headers, data=payload).json()

    return resp['id']


def read_department(_id: str) -> dict:
    headers = {
        'Id': _id
    }
    resp = requests.get(f"{url_prefix}departments", headers=headers).json()

    return resp


### TRANSACTIONS


def push_transaction(transaction: TransactionJSON) -> str:
    data = to_dict_recursive(transaction.__dict__)
    payload = json.dumps(data)

    resp = requests.post(f"{url_prefix}transactions", data=payload).json()

    return resp['id']


def read_transaction(_id: str) -> dict:
    headers = {
        'Id': _id
    }
    resp = requests.get(f"{url_prefix}transactions", headers=headers).json()

    return resp

# p = PersonJSON('Valerii', 'Nikitin', '01.01.1991', 'test addr')
# create_person(p)
