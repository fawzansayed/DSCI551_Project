import json
import requests
import pandas as pd

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

inp = input('Enter command: ')
a = inp.split()

resp = requests.get(url + a[1] + '.json').json()

for key, value in resp.items():
    endpoint = value

    _file = requests.get(value + '.json').json()

    # Reading the data from the file
    db = pd.read_json(_file)
    db.to_csv("output.csv", sep = '\t')
    print(db)