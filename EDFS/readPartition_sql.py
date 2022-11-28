import sqlite3
import pandas as pd

inp = input('Enter command: ')
a = inp.split()
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
temp=a[1].split('/')
cur.execute('''SELECT location FROM  partition WHERE file=? AND partition=?''',(temp[-1],int(a[2])))
rows=cur.fetchall()
cur.execute('''SELECT * FROM  "{}" '''.format(rows[0][0].replace('"', '""')))
ro=cur.fetchall()
cur.execute('PRAGMA table_info("{}")'.format(rows[0][0].replace('"', '""')))
r=cur.fetchall()
cols=[]
for tt in r :
    cols.append(tt[1])
df=pd.DataFrame(ro, columns=cols)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
conn.commit()
conn.close()
