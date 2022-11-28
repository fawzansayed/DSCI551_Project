import json
import sqlite3
import requests
import datetime
from EDFS.mkdir_firebase import *
from EDFS.ls_firebase import *
from flask import Flask, Response, request, make_response, jsonify, render_template
# from EDFS.firebase import *
# from EDFS.sqlite import *

sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


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
    app.run(debug=True)
    cursor.close()
