import json
import requests

def is_insult(text):
    # It only works when docker is runnig on a localhost
    res = requests.post('https://7006.lnsigo.mipt.ru/model', data=json.dumps({"x": [text]}))
    return  res.json()[0][0]
