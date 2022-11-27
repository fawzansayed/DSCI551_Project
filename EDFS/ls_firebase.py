import requests
import json

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"

inp = input('Enter command: ')
a = inp.split()
resp = requests.get(url + a[1] + '.json').json()
print(resp)
