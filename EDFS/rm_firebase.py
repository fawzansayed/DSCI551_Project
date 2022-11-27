import json
import requests
url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

inp = input('Enter command: ')
a = inp.split()
resp = requests.delete(url + a[1] + '.json').json()
<<<<<<< HEAD
metadata_resp= requests.delete(url + '/metadata' + a[1] + ".json").json()
=======
metadata_resp= requests.delete(url + 'metadata/' + a[1] + '.json').json()

>>>>>>> a7dade83a0ca8f02035cab449f8e0a446bd8d706
