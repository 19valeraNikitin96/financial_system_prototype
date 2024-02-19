import datetime
import json
import logging

import pymongo
import requests
from bson import ObjectId

from data_access import DBAccess, DBOperations, DBCreatePayload, DBUpdatePayload, DBReadPayload
from data_access.mongo import MongoSpecific


class TCSpecific(MongoSpecific):

    def __init__(self):
        super().__init__()
        self._priority = None
        self._created_at = None

    @property
    def priority(self) -> int:
        return self._priority

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at


class TCCreatePayload(DBCreatePayload, TCSpecific):

    def __init__(self, db_name: str, collection_name: str, data: dict, priority: int = 50):
        super().__init__(collection_name, data)
        self._db_name = db_name
        self._priority = priority


class TCUpdatePayload(DBUpdatePayload, TCSpecific):

    def __init__(self, db_name: str, collection_name: str, data: dict, _id: str, priority: int = 50):
        super().__init__(collection_name, data, _id)
        self._db_name = db_name
        self._priority = priority


class TCReadPayload(DBReadPayload, TCSpecific):

    def __init__(self, db_name: str, collection_name: str, _id: str, priority: int = 50):
        super().__init__(collection_name, _id)
        self._db_name = db_name
        self._priority = priority


class TCImpl(DBOperations):

    def __init__(self, tc_access: DBAccess, db_access: DBAccess):
        self._tc_access = tc_access
        self._clock_url = f"http://{tc_access.addr}:{tc_access.port}/mongodb"

        self._db_access = db_access

        self._db_inst = pymongo.MongoClient(f"mongodb://{db_access.addr}:{db_access.port}/")

    def create(self, payload: TCCreatePayload) -> str:
        headers = {
            'Database': payload.db_name,
            'Collection': payload.collection_name,
            'Priority': str(payload.priority),
            'CreatedAt': str(datetime.datetime.utcnow().isoformat()),
            'Content-Type': 'application/json'
        }

        res = requests.post(self._clock_url, headers=headers, data=json.dumps(payload.data))
        resp = json.loads(res.text)
        _id = resp['id']

        return _id

    def update(self, payload: TCUpdatePayload):
        logging.debug(f'Updating [{payload.db_name}][{payload.collection_name}][{payload.id}][{payload.data}]')
        headers = {
            'Id': payload.id,
            'Database': payload.db_name,
            'Collection': payload.collection_name,
            'Priority': str(payload.priority),
            'CreatedAt': str(datetime.datetime.utcnow().isoformat()),
            'Content-Type': 'application/json'
        }

        res = requests.put(self._clock_url, headers=headers, data=json.dumps(payload.data))
        resp = json.loads(res.text)
        _id = resp['id']

        return _id

    def read(self, payload: TCReadPayload) -> dict:
        logging.debug(f'Reading [{payload.db_name}][{payload.collection_name}][{payload.id}]')
        db = self._db_inst[payload.db_name]
        collection = db[payload.collection_name]

        doc = collection.find_one({'_id': ObjectId(payload.id)})
        if doc is not None:
            del doc['_id']

        return doc
