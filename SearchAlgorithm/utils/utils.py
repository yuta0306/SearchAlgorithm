import json

def load_json(path: str) -> dict:
    result = json.load(open(path, 'r'))
    
    return result