import sqlite3

def rm_sql(inp):
    a = inp.split()
    temp=a[1].split('/')
    conn = sqlite3.connect('../DSCI551_Project.sqlite')
    cur = conn.cursor()

    del_metadata='''DELETE FROM metadata WHERE folder = ?'''
    del_shape='''DELETE FROM shape WHERE child = ?'''
    cur.execute(del_metadata, (temp[-1],))
    cur.execute(del_shape, (temp[-1],))
    conn.commit()
    conn.close()
    res = "Successfully deleted {}".format(temp[-1])
    return res
