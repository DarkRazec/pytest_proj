def get_val(collection: dict, key, default='git'):
    if key in collection.keys():
        return collection.get(key)
    return default
