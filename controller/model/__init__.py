
class DocumentBase:

    def __init__(self):
        self._id = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def doc(self) -> dict:
        doc = dict(self.__dict__)
        del doc['_id']

        return doc
