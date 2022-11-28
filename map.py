import sqlite3
import pandas as pd
import requests

inp1 = input('Enter File Location: ')
inp2 = input('Enter Column: ')
inp3 = input('Enter Query (equal,greater,lesser,greatere,lessere): ')
inp4 = input('Enter Value: ')

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"
resp = requests.get(url + inp1 + '.json').json()

first=0
for key, value in resp.items():
    _file = requests.get(value + '.json').json()
    if first==0 :
        df = pd.DataFrame(_file)
    else :
        df=df.append(pd.DataFrame(_file), ignore_index=True)
    first=1


if df[inp2].dtypes!='object' :
    inp4=int(inp4)

if inp3=='equal' :
    out=df[df[inp2]==inp4]
elif inp3=='greater' :
    out=df[df[inp2]>inp4]
elif inp3=='lesser' :
    out=df[df[inp2]<inp4]
elif inp3=='greatere' :
    out=df[df[inp2]>=inp4]
elif inp3=='lessere' :
    out=df[df[inp2]<=inp4]

print(out)
