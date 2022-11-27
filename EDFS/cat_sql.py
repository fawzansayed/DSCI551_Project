import sqlite3

inp = input('Enter command: ')
a = inp.split()
temp=a[1].split('/')
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM  "{}" '.format(temp[-1].replace('"', '""')))
r=cur.fetchall()
print(r)
conn.commit()
conn.close()
