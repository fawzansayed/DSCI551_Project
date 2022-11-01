import json
import requests

if __name__ == '__main__':
    data=pd.read_csv('Data/List of Orders.csv')
    data.set_index('Order ID', inplace=True)
    data=data.to_dict('index')

    url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/List_of_Orders.json"
    resp = requests.put(url, json.dumps(data))
    print(resp)


    data1=pd.read_csv('Data/Sales target.csv')
    data1=data1.to_dict('index')

    url = "https://dsci551project-1ff87-default-rtdb.firebaseio.com/Sales_Target.json"
    resp1 = requests.put(url, json.dumps(data1))
    print(resp1)