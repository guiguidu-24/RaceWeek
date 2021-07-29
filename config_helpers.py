from json import loads


def get_dict_data(path):
    with open(path, 'r') as stream_file:
        data = stream_file.read()
    return loads(data)


def get_data(path: str, id: str):
    return get_dict_data(path)[id]

