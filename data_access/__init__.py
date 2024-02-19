from dataclasses import dataclass


@dataclass
class DBAccess:
    addr: str
    port: int


class DBPayloadBase:

    def __init__(self, collection_name: str):
        self._collection_name = collection_name

    @property
    def collection_name(self) -> str:
        return self._collection_name


class DBPushPayload(DBPayloadBase):

    def __init__(self, collection_name: str, data: dict):
        super().__init__(collection_name)
        self._data = data

    @property
    def data(self) -> dict:
        return dict(self._data)


class DBCreatePayload(DBPushPayload):
    pass


class DBUpdatePayload(DBPushPayload):

    def __init__(self, collection_name: str, data: dict, _id: str):
        super().__init__(collection_name, data)
        self._id = _id

    @property
    def id(self) -> str:
        return self._id


class DBReadPayload(DBPayloadBase):

    def __init__(self, collection_name: str, _id: str):
        super().__init__(collection_name)
        self._id = _id

    @property
    def id(self) -> str:
        return self._id


class DBOperations:

    def create(self, payload: DBCreatePayload) -> str: ...

    def read(self, payload: DBReadPayload) -> dict: ...

    def update(self, payload: DBUpdatePayload) -> str: ...

    # def delete(self, payload: DB): ...


class Collection:

    def __init__(self, collection_name: str):
        self._collection_name = collection_name

    @property
    def collection_name(self) -> str:
        return self._collection_name
