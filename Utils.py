import logging

logging.basicConfig(level="INFO")

def loadconfig(filename):
    import json
    json_data  = {}
    with open(filename) as f:
        json_data = json.load(f)
    return json_data

def readfile(filename):
    datas = []
    with open(filename) as f:
        datas = f.readlines()

    return datas
