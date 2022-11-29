import sqlite3

def ls_sql(inp):
    a = inp.split()
    temp=a[1].split('/')
    conn = sqlite3.connect('DSCI551_Project.sqlite')
    cur = conn.cursor()
    if temp[-1]=='' :
        temp[-1]='root'
    r = cur.execute('''SELECT child FROM shape WHERE parent=?''',(temp[-1],))
    r = cur.fetchall()
    if len(r)==0 :
        res='Nothing in the location!'
    else :
        res=''
        for ele in r :
            res+=ele[0]+'\n'
    conn.commit()
    conn.close()
    return res
