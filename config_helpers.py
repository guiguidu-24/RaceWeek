import json


def get_dict_data(path):
    with open(path, 'r') as stream_file:
        data = stream_file.read()
    return json.loads(data)


def get_data(path, id):
    return get_dict_data(path)[id]

