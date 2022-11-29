import requests
import json

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"

def gpl(inp):
    a = inp.split()
    resp = requests.get(url + a[1] + '.json').json()
    res = ''

    for k in resp.keys() :
        res = res + (k +': ' +resp[k] + '\n')

    return res