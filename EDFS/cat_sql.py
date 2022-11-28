import sqlite3
import pandas as pd
inp = input('Enter command: ')
a = inp.split()
temp=a[1].split('/')
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
data=cur.execute('SELECT * FROM  "{}" '.format(temp[-1].replace('"', '""')))
r=cur.fetchall()
for column in data.description:
    c=column[0].to_list()
df=pd.DataFrame(columns=c)
for rows in r:
    row=rows.split(',')
    df.iloc[len(df)]=row
print(df)
conn.commit()
conn.close()
