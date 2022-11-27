import json
import requests
import pandas as pd

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"

inp = input('Enter command: ')
a = inp.split()

resp = requests.get(url + a[1] + '.json').json()

first=0
for key, value in resp.items():
    endpoint = value
    _file = requests.get(value + '.json').json()
    if first==0 :
        df = pd.DataFrame(_file)
    else :
        df=df.append(pd.DataFrame(_file), ignore_index=True)
    first=1
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
