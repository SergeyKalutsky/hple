import json
import requests

def is_insult(text):
    # It only works when docker is runnig on a localhost
    res = requests.post('http://127.0.0.1:5555/model', data=json.dumps({"x": [text]}))
    return  res.json()[0][0]

is_insult('hello')