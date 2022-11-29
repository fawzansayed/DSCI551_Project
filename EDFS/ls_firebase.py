import json
import requests

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

def ls(inp):
    a = inp.split()
    root = 'root'

    resp = requests.get(url + root + a[1] + '.json').json()
    res = json.dumps(resp , indent = 4)
    return str(res)

if __name__ == '__main__':
    ls()