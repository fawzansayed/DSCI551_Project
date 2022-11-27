import requests
from datetime import datetime

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

inp = input('Enter command: ')
a = inp.split()
new = a[1].split('/')[-1]
dir = a[1].split('/')[1:-1]
root_dir = 'root'

# Establishing the metadata directory and getting the current time
metadata = '/metadata'
time = datetime.now().strftime('%m/%d/%Y')

if len(dir) != 0:
    for a in dir:
        root_dir = root_dir + '/' + a

if requests.get(url + root_dir + '/.json').status_code != 200 :
    print('root_dirctory not found!')
    exit()

resp = requests.patch(url + root_dir + '/.json', json = {new:''})
metadata_resp = requests.patch(url + metadata + '/.json', json = time)
