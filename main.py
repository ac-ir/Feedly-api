import requests, os
from pprint import pprint

class Feedly():

    def __init__(self):
        self.url = "https://cloud.feedly.com"
        self.token = os.environ.get('token')

    def profile(self):
        self.endpoint ="/v3/profile"
        self.get()

    def search(self, query):
        self.endpoint = f"/v3/search/contents?streamId=:replace_with_id&query={query}"
        self.get()

    def collections(self):
        self.endpoint="/v3/collections"
        self.get()
    def get(self):
        r = requests.get(self.url + self.endpoint, headers={'Authorization': 'Bearer ' + self.token})
        pprint(r.json())


if __name__ == "__main__":
    f = Feedly()
    f.collections()