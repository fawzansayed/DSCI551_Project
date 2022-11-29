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
from EDFS.GPL_firebase import *
from EDFS.readPartition_firebase import *

from EDFS.mkdir_sql import *
from EDFS.ls_sql import *
from EDFS.cat_sql import *
from EDFS.put_sql import *
from EDFS.rm_sql import *
from EDFS.GPL_sql import *
from EDFS.readPartition_sql import *

from pandas import DataFrame, read_csv
from flask import Flask, Response, request, make_response, jsonify, render_template, redirect

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

@app.route('/table', methods=['GET'])
def table():
    conn = sqlite3.connect('DSCI551_Project.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    r = cur.fetchall() 
    return render_template('table.html', table=r)

@app.route('/mkdir_sql', methods=['GET'])
def _mkdir_sql():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = mkdir_sql(inp)
        return render_template('ls_sql.html', path=path, inp=inp)

@app.route('/ls_sql', methods=['GET'])
def _ls_sql():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = ls_sql(inp)
        return render_template('ls_sql.html', path=path, inp=inp)

@app.route('/cat_sql', methods=['GET'])
def _cat_sql():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = cat_sql(inp)
        return render_template('cat_sql.html', path=path, inp=inp)

@app.route('/put_sql', methods=['GET'])
def _put_sql():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = put_sql(inp)
        return render_template('put_sql.html', path=path, inp=inp)

@app.route('/rm_sql', methods=['GET'])
def _rm_sql():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = rm_sql(inp)
        return render_template('rm_sql.html', path=path, inp=inp)

@app.route('/mkdir', methods=['GET'])
def mkdir_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = mkdir(inp)
        return render_template('mkdir.html', path=path, inp=inp)

@app.route('/help', methods=['GET'])
def help():
    if request.method == 'GET':
        return render_template('help.html')  


@app.route('/ls', methods=['GET'])
def ls_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = ls(inp)
        print(path)
        return render_template('ls.html', path=path, inp=inp)


@app.route('/cat', methods=['GET'])
def cat_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = cat(inp)
        return render_template('cat.html', path=path, inp=inp)


@app.route('/put', methods=['GET'])
def put_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = put(inp)
        return render_template('put.html', path=path, inp=inp)


@app.route('/rm', methods=['GET'])
def rm_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = rm(inp)
        return render_template('rm.html', path=path, inp=inp) 

@app.route('/gpl', methods=['GET'])
def gpl_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = gpl(inp)
        return render_template('gpl.html', path=path, inp=inp)

@app.route('/readPartition', methods=['GET'])
def partition_firebase():
    if request.method == 'GET':
        inp = request.args.get('command')
        path = readPartition(inp)
        return render_template('partition.html', path=path, inp=inp)

if __name__ == '__main__':
    app.run(debug = True, port = 5002)
    
    cursor.close()
