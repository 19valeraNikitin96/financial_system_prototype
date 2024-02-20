import logging

import pymongo
from bson import ObjectId
from pymongo import ReadPreference
from typing import List

from data_access import DBAccess, DBOperations, DBCreatePayload, DBUpdatePayload, DBReadPayload


class MongoSpecific:

    def __init__(self):
        self._db_name = None

    @property
    def db_name(self) -> str:
        return self._db_name


class MongoCreatePayload(DBCreatePayload, MongoSpecific):

    def __init__(self, db_name: str, collection_name: str, data: dict):
        super().__init__(collection_name, data)
        self._db_name = db_name


class MongoUpdatePayload(DBUpdatePayload, MongoSpecific):

    def __init__(self, db_name: str, collection_name: str, data: dict, _id: str):
        super().__init__(collection_name, data, _id)
        self._db_name = db_name


class MongoReadPayload(DBReadPayload, MongoSpecific):

    def __init__(self, db_name: str, collection_name: str, _id: str):
        super().__init__(collection_name, _id)
        self._db_name = db_name


class MongoReplicaSetImpl(DBOperations):
    _instance = None

    def __init__(self, accesses: List[DBAccess]):
        self._accesses = accesses
        conn_str = ','.join([f"{access.addr}:{access.port}" for access in accesses])
        self._replica_set = pymongo.MongoClient(f"mongodb://{conn_str}/?replicaSet=my-mongo-set", w=8, read_preference=ReadPreference.SECONDARY_PREFERRED)

    def create(self, payload: MongoCreatePayload):
        logging.debug(f'Creating [{payload.db_name}][{payload.collection_name}][{payload.data}]')
        db = self._replica_set[payload.db_name]
        collection = db[payload.collection_name]

        data = payload.data
        _id = ObjectId()
        data['_id'] = _id
        collection.insert_one(data)
        res = collection.find({})
        print(res)

        return str(_id)

    def update(self, payload: MongoUpdatePayload) -> str:
        logging.debug(f'Updating [{payload.db_name}][{payload.collection_name}][{payload.id}][{payload.data}]')
        db = self._replica_set[payload.db_name]
        collection = db[payload.collection_name]

        collection.update_one(
            {'_id': ObjectId(payload.id)},
            {'$set': payload.data}
        )
        return payload.id

    def read(self, payload: MongoReadPayload) -> dict:
        logging.debug(f'Reading [{payload.db_name}][{payload.collection_name}][{payload.id}]')
        db = self._replica_set[payload.db_name]
        collection = db[payload.collection_name]

        doc = collection.find_one({'_id': ObjectId(payload.id)})
        if doc is not None:
            del doc['_id']

        return doc


def get_mongo_driver(accesses: List[DBAccess]) -> MongoReplicaSetImpl:
    return MongoReplicaSetImpl(accesses)
