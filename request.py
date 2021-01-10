import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = ['Female',21,1.62,64,'yes','no',2,3,'Sometimes','no',2,'no',0,1,'no','Public_Transportation']

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)