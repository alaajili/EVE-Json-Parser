import json

def eve_parser(path: str):
    with open(path, 'r') as f:
        data = json.load(f)

eve_parser('./test.json')

