import sqlite3

inp = input('Enter command: ')
a = inp.split()
temp=a[1].split('/')
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT * from  ?''', (temp[-1],))
conn.commit()
conn.close()