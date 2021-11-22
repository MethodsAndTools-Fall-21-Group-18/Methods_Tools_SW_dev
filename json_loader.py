import json

def decode_json(filename):
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data