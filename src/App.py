import json
import sqlite3
import requests
import datetime
from spark import main
from flask import Flask, Response, request, make_response

sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/sqlite', methods=[GET])
def sql():
    # The main query to show all of the data in one location
    table = request.args.get('table')
    initial_query = "SELECT COLUMN_NAME FROM WHERE table_name = '"+table+"' and table_schema = ''"

    # Finding specific values in the database from the keyword
    if request.args.get('keyword'):
        keycol = request.args.get('column')
        keyword = request.args.get('keyword')
        key_query = "SELECT * FROM project."+table+" WHERE " + keycol + " LIKE '%" + keyword + "%'"
    else:
        key_query = "SELECT * FROM project." + table

    # Ordering specific values in the database based on the options they choose
    if request.args.get('order'):
        order_query = key_query + " ORDER BY " + request.args.get("order")

    # Grouping specific values in the database based on the options they choose
    if request.args.get('group'):
        group_query = key_query + " GROUP BY " + request.args.get("group")

    return response 

if __name__ == '__main__':
    app.run()
    cursor.close()