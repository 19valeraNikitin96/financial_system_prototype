
class DocumentBase:

    def __init__(self):
        self._id = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def doc(self) -> dict:
        doc = DocumentBase.to_dict_recursive(dict(self.__dict__))

        return doc

    @staticmethod
    def to_dict_recursive(src: dict, acc: dict = None) -> dict:
        if acc is None:
            acc = dict()

        for key, value in src.items():
            if key == '_id':
                continue

            if isinstance(value, dict):
                acc[key] = DocumentBase.to_dict_recursive(value, acc)
            elif hasattr(value, '__dict__'):
                acc[key] = DocumentBase.to_dict_recursive(value.__dict__, dict())
            else:
                acc[key] = value

        return acc
