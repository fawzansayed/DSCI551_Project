import sqlite3
import pandas as pd
from datetime import datetime


def put_sql(inp) :
    a = inp.split()
    data=pd.read_csv('../Data/'+a[1])
    aaa=a[1].split('.')[0]
    conn = sqlite3.connect('../DSCI551_Project.sqlite')
    cur = conn.cursor()

    if int(a[3])==1:
        data.to_sql(name=aaa, con=conn, index=False)
        cur.execute('''INSERT INTO partition VALUES ( ?, ?, ?)''',(aaa,1,aaa) )

    else :
        lo=0
        for i in range(0,int(a[3])) :
            up=lo+int(len(data)/int(a[3]))
            block=data.iloc[lo:up]
            block.reset_index(drop=True, inplace=True)
            lo=up
            block.to_sql(name=aaa+str(i+1), con=conn, index=False)
            cur.execute('''INSERT INTO partition VALUES ( ?, ?, ?)''',(aaa,(i+1),aaa+str(i+1)) )


    t=a[2].split('/')
    if len(t)==1 :
        par='root'
    else :
        par=t[-1]
    time = datetime.now().strftime('%Y-%m-%d')
    cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',(aaa,time) )
    cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',(par,aaa) )
    conn.commit()
    conn.close()
    res = 'Successfully put'
    return res
