import sqlite3

conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS metadata' )
cur.execute('''
CREATE TABLE metadata (
    folder   VARCHAR(20),
    createtime  DATE
);
''')

cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',('root','2022-9-10') )
cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',('user','2022-9-10') )
cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',('jack','2022-11-10') )
cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',('work','2022-11-10') )
cur.execute('''INSERT INTO metadata VALUES ( ?, ?)''',('OrderDetails','2022-11-10') )
cur.execute('DROP TABLE IF EXISTS shape' )
cur.executescript('''
CREATE TABLE shape (
    parent   VARCHAR(20),
    child VARCHAR(20)
);
''')
cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',('root','user') )
cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',('user','jack') )
cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',('user','work') )
cur.execute('''INSERT INTO shape VALUES ( ?, ?)''',('work','OrderDetails') )
cur.execute('DROP TABLE IF EXISTS partition' )
cur.executescript('''
CREATE TABLE partition (
    file   VARCHAR(20),
    partition INT,
    location VARCHAR(50)
);
''')
cur.execute('''INSERT INTO partition VALUES ( ?, ?, ?)''',('OrderDetails', 1, 'OrderDetails') )
conn.commit()
conn.close()
