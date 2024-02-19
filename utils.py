

def to_dict_recursive(src: dict, acc: dict = None) -> dict:
    if acc is None:
        acc = dict()

    for key, value in src.items():
        if key == '_id':
            continue

        if isinstance(value, dict):
            acc[key] = to_dict_recursive(value, acc)
        elif hasattr(value, '__dict__'):
            acc[key] = to_dict_recursive(value.__dict__, dict())
        else:
            acc[key] = value

    return acc
