import json
import requests
import pandas as pd
from datetime import datetime

def put(inp):
    a = inp.split()
    data=pd.read_csv('Data/'+a[1])
    aaa=a[1].split('.')[0]
    data1=data.to_dict('index')
    
    url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/"
    lo=0
    j={}
    if int(a[3])==1:
        resp = requests.put(url+aaa+'.json', json.dumps(data1))
        j['p1']=url+aaa
    else :
        for i in range(0,int(a[3])) :
            up=lo+int(len(data)/int(a[3]))
            block=data.iloc[lo:up]
            block.reset_index(drop=True, inplace=True)
            block1=block.to_dict('index')
            lo=up
            resp = requests.put(url+aaa+str(i+1)+'.json', json.dumps(block1))
            j['p'+str(i+1)]=url+aaa+str(i+1)
    
    if len(a[2].split('/'))==1 :
        resp = requests.patch(url+'root/'+aaa+'.json', json = j)
    else :
        resp = requests.patch(url+'root'+a[2]+'/'+aaa+'.json', json = j)
    
    time = datetime.now().strftime('%m/%d/%Y')
    resp = requests.patch(url+'metadata/.json', json = {aaa:time})
    res = 'Successfully put'
    return res
if __name__ == '__main__':
    put()