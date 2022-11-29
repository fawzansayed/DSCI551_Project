import json
import requests

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

def rm(inp):
    a = inp.split()
    b = a[1].split('/')

    resp = requests.delete(url + 'root' + a[1] + '.json').json()
    metadata_resp = requests.delete(url + 'metadata/' + b[-1] + '.json').json()
    res = "Successfully deleted {}".format(b[1])
    return res


if __name__ == '__main__':
    rm()
