import json
import sqlite3
import requests
import datetime
import pandas as pd
from EDFS.mkdir_firebase import *
from EDFS.ls_firebase import *
from EDFS.cat_firebase import *
from EDFS.put_firebase import *
from EDFS.rm_firebase import *
from pandas import DataFrame, read_csv
from flask import Flask, Response, request, make_response, jsonify, render_template

conn = sqlite3.connect('DSCI551_Project.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route("/search")
def search():
    return render_template("search.html", title="Search")

@app.route("/explore")
def explore():
    return render_template("explore.html", title="Explore")

@app.route('/explore/table')
def table():
    conn = sqlite3.connect('DSCI551_Project.sqlite')
    conn.row_factory = sqlite3.Row
    print("Opened successfully in table route")
    cur = conn.cursor()

    cur.execute('''SELECT * FROM OrderDetails ''')
    r = cur.fetchall()

    return render_template('table.html', table=r)


@app.route('/mkdir', methods=['GET'])
def mkdir_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = mkdir(inp)
        return path


@app.route('/ls', methods=['GET'])
def ls_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = ls(inp)
        return path


@app.route('/cat', methods=['GET'])
def cat_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = cat(inp)
        return path


@app.route('/put', methods=['GET'])
def put_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = put(inp)
        return path


@app.route('/rm', methods=['GET'])
def rm_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = rm(inp)
        return path


# @app.route('/display_table', methods=['GET'])
# def html_table():
#     return render_template('index.html',


# file = 'Data/List of Orders.csv'
# df = pd.read_csv(file)
# df.to_html(header="true", table_id="main_table")

# @app.route('/sqlite', methods=[GET])
# def sql():
#     # The main query to show all of the data in one location
#     table = request.args.get('table')
#     initial_query = "SELECT COLUMN_NAME FROM WHERE table_name = '"+table+"' and table_schema = ''"

#     # Finding specific values in the database from the keyword
#     if request.args.get('keyword'):
#         keycol = request.args.get('column')
#         keyword = riquest.args.get('keyword')
#         key_query = "SELECT * FROM project."+table+" WHERE " + keycol + " LIKE '%" + keyword + "%'"
#     else:
#         key_query = "SELECT * FROM project." + table

#     # Ordering specific values in the database based on the options they choose
#     if request.args.get('order'):
#         order_query = key_query + " ORDER BY " + request.args.get("order")

#     # Grouping specific values in the database based on the options they choose
#     if request.args.get('group'):
#         group_query = key_query + " GROUP BY " + request.args.get("group")

#     return response


if __name__ == '__main__':
    app.run(debug = True, port = 5002)
    
    cursor.close()
