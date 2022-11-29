import sqlite3
import pandas as pd
import requests

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"
def map(input) :
    inp=input.split()
    resp = requests.get(url + inp[0] + '.json').json()
    first=0
    for key, value in resp.items():
        _file = requests.get(value + '.json').json()
        if first==0 :
            df = pd.DataFrame(_file)
        else :
            df=df.append(pd.DataFrame(_file), ignore_index=True)
        first=1

    if df[inp[1]].dtypes!='object' :
        inp[3]=int(inp[3])

    if inp[2]=='equal' :
        out=df[df[inp[1]]==inp[3]]
    elif inp[2]=='greater' :
        out=df[df[inp[1]]>inp[3]]
    elif inp[2]=='lesser' :
        out=df[df[inp[1]]<inp[3]]
    elif inp[2]=='greatere' :
        out=df[df[inp[1]]>=inp[3]]
    elif inp[2]=='lessere' :
        out=df[df[inp[1]]<=inp[3]]

    if inp[4]=='count' :
        return out.shape[0]
    elif inp[4]=='min' :
        return out[inp[5]].min()
    elif inp[4]=='max' :
        return out[inp[5]].max()
    elif inp[4]=='sum' :
        return out[inp[5]].sum()
    elif inp[4]=='avg' :
        return out[inp[5]].mean()

inn=input('Enter Command: ')
print(map(inn))
