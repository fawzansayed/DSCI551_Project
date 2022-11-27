import sqlite3

inp = input('Enter command: ')
a = inp.split()
temp=a[1].split('/')
conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
if temp[-1]=='' :
    temp[-1]='root'
cur.execute('''SELECT child FROM shape WHERE parent=?''',(temp[-1],))
r = cur.fetchall()
if len(r)==0 :
    print('Nothing in the location!')
else :
    for ele in r :
        print(ele[0])
conn.commit()
conn.close()
