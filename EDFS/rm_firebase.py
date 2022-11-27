import json
import requests
url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

inp = input('Enter command: ')
a = inp.split()
<<<<<<< HEAD
resp = requests.delete(url + 'root' + a[1] + '.json').json()
metadata_resp= requests.delete(url + 'metadata' + a[1] + '.json').json()
=======
resp = requests.delete(url + a[1] + '.json').json()
<<<<<<< HEAD
metadata_resp= requests.delete(url + '/metadata' + a[1] + ".json").json()
=======
metadata_resp= requests.delete(url + 'metadata/' + a[1] + '.json').json()
>>>>>>> e5989e5ee87cea889104eeac01509a4ee7fc53f9

>>>>>>> a7dade83a0ca8f02035cab449f8e0a446bd8d706
