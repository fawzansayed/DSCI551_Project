import sqlite3
from datetime import datetime

def mkdir_sql(inp):
    a = inp.split()
    temp=a[1].split('/')
    conn = sqlite3.connect('DSCI551_Project.sqlite')
    cur = conn.cursor()
    if temp[-2]=='' :
        temp[-2]='root'
    time = datetime.now().strftime('%Y-%m-%d')
    cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',(temp[-1],time) )
    cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',(temp[-2],temp[-1]) )
    res = 'Successfully created {} at {}'.format(temp[-1], time)
    conn.commit()
    conn.close()
    return res
