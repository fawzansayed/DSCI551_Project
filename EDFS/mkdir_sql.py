import sqlite3
from datetime import datetime

inp = input('Enter command: ')
a = inp.split()
temp=a[1].split('/')
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
if temp[-2]=='' :
    temp[-2]='root'
time = datetime.now().strftime('%Y-%m-%d')
cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',(temp[-1],time) )
cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',(temp[-2],temp[-1]) )
conn.commit()
conn.close()
