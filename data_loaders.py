import json


def load_from_json(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        try:
            return json.load(file_object)
        except json.decoder.JSONDecodeError:
            return None
