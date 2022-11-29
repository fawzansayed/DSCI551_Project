import requests
import json
import pandas as pd

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

def readPartition(inp):
    a = inp.split()
    resp = requests.get(url + 'root' + a[1] + '.json').json()
    loc=resp['p'+a[2]]
    out=requests.get(loc + '.json').json()
    df = pd.DataFrame(out)
    return df
