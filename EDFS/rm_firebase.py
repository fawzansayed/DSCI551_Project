import json
import requests
url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

inp = input('Enter command: ')
a = inp.split()
b=a[1].split('/')
resp = requests.delete(url + 'root' + a[1] + '.json').json()
metadata_resp= requests.delete(url + 'metadata/' + b[-1] + '.json').json()

