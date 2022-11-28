import json
import requests

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/root"

def ls():
    a = inp.split()
    resp = requests.get(url + a[1] + '.json').json()

    res = json.dump(resp)
    return res

if __name__ == '__main__':
    ls()