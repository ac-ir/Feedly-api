import requests, os
from pprint import pprint


url = "https://cloud.feedly.com/v3/profile"
token = os.environ.get('token')

r = requests.get(url, headers={'Authorization': 'Bearer ' + token})
pprint(r.json())
