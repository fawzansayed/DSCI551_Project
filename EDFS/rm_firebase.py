import json
import requests
url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"

inp = input('Enter command: ')
a = inp.split()
resp = requests.delete(url + a[1] + '.json').json()
metadata_resp= requests.delete(url + '/metadata' + a[1] + ".json").json()
