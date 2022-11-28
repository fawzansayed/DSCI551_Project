import pandas as pd
import sqlite3
import json

inp1 = input('Enter File Location: ')
temp=inp1.split('/')
inp2 = input('Enter Column: ')
inp3 = input('Enter Query (equal,greater,lesser,greatere,lessere): ')
inp4 = input('Enter Value: ')
conn = sqlite3.connect('DSCI551_Project.sqlite')
cur = conn.cursor()

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
conn.commit()
conn.close()
