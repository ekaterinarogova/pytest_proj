def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение по умалчанию
    :param collection: исходная библиотека
    :param key: ключ для поиска значения
    :param default: значение по умалчанию
    :return: значение по заданному ключу
    """
    if key not in collection.keys():
        return default

    return collection[key]
