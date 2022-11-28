import sqlite3

inp = input('Enter command: ')
a = inp.split()
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
temp=a[1].split('/')
cur.execute('SELECT location FROM  partition WHERE file="{}"'.format(temp[-1].replace('"', '""')))
rows=cur.fetchall()
i=1
for r in rows :
    print('p%d: %s' % (i,r[0]))
    i+=1

conn.commit()
conn.close()
