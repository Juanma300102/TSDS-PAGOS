def get_all_keys(obj: dict = None, items: list = None):
    if not items:
        items = obj.items()
    return list(map(lambda item: item[0], items))
