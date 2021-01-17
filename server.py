from flask import Flask, render_template #追加
import pymysql #追加
import time
import datetime
from flask import render_template, url_for
from flask import request
import numpy 
import json

app = Flask(__name__)

@app.route('/')
def hello():
    #db setting
    db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            db='temperature',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    cur = db.cursor()
    day = datetime.date.today()
    print(day)
    sql = "SELECT * FROM `temperature` WHERE `day`="+"'"+str(day)+"'" +"ORDER BY `time` DESC LIMIT 1"
    cur.execute(sql)
    members = cur.fetchall()
    print(members)
    cur.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members) #変更

app.run(port="8082")