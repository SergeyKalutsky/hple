import json
import requests

def is_insult(text):
    res = requests.post('http://127.0.0.1:5555/model', data=json.dumps({"x": [text]}))
    return  res.json()[0][0]

is_insult('hello')