import sqlite3

def GPL_sql(inp):
    a = inp.split()
    conn = sqlite3.connect('../DSCI551_Project.sqlite')
    cur = conn.cursor()
    temp=a[1].split('/')
    cur.execute('SELECT location FROM  partition WHERE file="{}"'.format(temp[-1].replace('"', '""')))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    i=1
    res=''
    for r in rows :
        res = res + (i +': ' +r[0] + '\n')
        i+=1

    return res
