import json
import logging

from data_access import DBOperations, DBCreatePayload, DBAccess, DBUpdatePayload, DBReadPayload
from data_access.autumn_db.db_driver import DBDriver, CollectionName, Document, DocumentId


class AutumnDBImpl(DBOperations):

    def __init__(self, db_access: DBAccess):
        self._db_access = db_access
        self._db_driver = DBDriver(db_access.addr, db_access.port)

    def create(self, payload: DBCreatePayload) -> str:
        _id = self._db_driver.create_document(CollectionName(payload.collection_name), Document(json.dumps(payload.data)))
        return _id

    def update(self, payload: DBUpdatePayload) -> str:
        self._db_driver.update_document(
            CollectionName(payload.collection_name),
            DocumentId(payload.id),
            Document(json.dumps(payload.data))
        )

        return payload.id

    def read(self, payload: DBReadPayload) -> dict:
        while True:
            try:
                doc = self._db_driver.read_document(
                    CollectionName(payload.collection_name),
                    DocumentId(payload.id),
                )
                return json.loads(doc.document)
            except Exception as e:
                logging.warning(e)
