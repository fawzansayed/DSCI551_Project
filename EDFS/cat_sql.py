import sqlite3
import pandas as pd
inp = input('Enter command: ')
a = inp.split()
temp=a[1].split('/')
conn = sqlite3.connect('../DSCI551_Project.sqlite')
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
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
conn.commit()
conn.close()
