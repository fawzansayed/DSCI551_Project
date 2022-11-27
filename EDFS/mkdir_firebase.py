import requests

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"

inp=input('Enter command: ')
a=inp.split()
new=a[1].split('/')[-1]
dir=a[1].split('/')[1:-1]
dire='root'
if len(dir)!=0:
    for a in dir:
        dire=dire+'/'+a

if requests.get(url+dire+'/.json').status_code != 200 :
    print('Directory not found!')
    exit()

resp = requests.patch(url+dire+'/.json',json={new:''})
