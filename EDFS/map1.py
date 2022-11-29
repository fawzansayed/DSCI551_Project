import pandas as pd
import sqlite3
import json

def map1(input) :
    conn = sqlite3.connect('../DSCI551_Project.sqlite')
    cur = conn.cursor()
    inp=input.split()
    temp=inp[0].split('/')
    cur.execute('SELECT count(*) FROM  partition WHERE file="{}"'.format(temp[-1].replace('"', '""')))
    rr=cur.fetchone()

    if int(rr[0])==1 :
        cur.execute('SELECT * FROM  "{}" '.format(temp[-1].replace('"', '""')))
        rows=cur.fetchall()
        cur.execute('PRAGMA table_info("{}")'.format(temp[-1].replace('"', '""')))
        r=cur.fetchall()
        cols=[]
        for tt in r :
            cols.append(tt[1])
        df=pd.DataFrame(rows, columns=cols)
    else :
        first=0
        for i in range(0,int(rr[0])) :
            tempo=temp[-1]+str(i+1)
            cur.execute('SELECT * FROM  "{}" '.format(tempo.replace('"', '""')))
            rows=cur.fetchall()
            if first==0:
                cur.execute('PRAGMA table_info("{}")'.format(tempo.replace('"', '""')))
                r=cur.fetchall()
                cols=[]
                for tt in r :
                    cols.append(tt[1])
                df=pd.DataFrame(rows, columns=cols)
                first=1
            else :
                df=df.append(pd.DataFrame(rows, columns=cols), ignore_index=True)


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
        return out[inp[5]].avg()
    conn.commit()
    conn.close()

inn=input('Enter Command: ')
print(map1(inn))
