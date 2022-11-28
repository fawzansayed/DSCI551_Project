import requests
import json
import pandas as pd
import sqlite3


data=pd.read_csv('../Data/List of Orders.csv')
data.set_index('Order ID', inplace=True)
data=data.to_dict('index')

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/List_of_Orders.json"
resp = requests.put(url, json.dumps(data))
print(resp)


data1=pd.read_csv('../Data/Sales target.csv')
data1=data1.to_dict('index')

url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/Sales_Target.json"
resp1 = requests.put(url, json.dumps(data1))
print(resp1)


conn = sqlite3.connect('../DSCI551_Project.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS OrderDetails' )
cur.executescript('''
CREATE TABLE OrderDetails (
    Order_ID   VARCHAR(7),
    Amount  INT,
    Profit  INT,
    Quantity   INT,
    Category   VARCHAR(11),
    Sub_Category   VARCHAR(16)
);
''')

data2=pd.read_csv('../Data/Order Details.csv')
for row in data2.itertuples(index=False):
    cur.execute('''INSERT INTO OrderDetails VALUES ( ?, ?, ?, ?, ?, ? )''',
            (row[0],row[1],row[2],row[3],row[4],row[5]) )

conn.commit()
print('Data Loaded to SQL successfully')
conn.close()
