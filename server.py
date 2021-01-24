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

@app.route('/hello.html')
def hello1():
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
    cur1 = db.cursor()
    cur2 = db.cursor()
    cur3 = db.cursor()
    cur4 = db.cursor()
    cur5 = db.cursor()
    cur6 = db.cursor()
    day = datetime.date.today()
    day1 =  datetime.date.today() - datetime.timedelta(days=1)
    day2 =  datetime.date.today() - datetime.timedelta(days=2)
    day3 =  datetime.date.today() - datetime.timedelta(days=3)
    day4 =  datetime.date.today() - datetime.timedelta(days=4)
    day5 =  datetime.date.today() - datetime.timedelta(days=5)
    print(day1)
    print(day2)
    print(day3)
    print(day4)
    print(day5)
    #sql = "SELECT avg(temperature) as temperature FROM `temperature`"
    sql = "SELECT * FROM `temperature` WHERE `day`="+"'"+str(day)+"'" +"ORDER BY `time` DESC LIMIT 1"
    sql1="SELECT day , DATE_FORMAT(time, '%H') as time, avg(temperature) as avg FROM temperature WHERE day='2021-01-18' GROUP BY DATE_FORMAT(time, '%H');"
    tday1="select avg(temperature) as temperature from temperature WHERE day='"+str(day1)+"';"
    tday2="select avg(temperature) as temperature from temperature WHERE day='"+str(day2)+"';"
    tday3="select avg(temperature) as temperature from temperature WHERE day='"+str(day3)+"';"
    tday4="select avg(temperature) as temperature from temperature WHERE day='"+str(day4)+"';"
    tday5="select avg(temperature) as temperature from temperature WHERE day='"+str(day5)+"';"
    cur.execute(sql)
    cur1.execute(sql1)
    cur2.execute(tday1)
    cur3.execute(tday2)
    cur4.execute(tday3)
    cur5.execute(tday4)
    cur6.execute(tday5)
    members = cur.fetchall()
    members1 = cur1.fetchall()
    today1 = cur2.fetchall()
    today2 = cur3.fetchall()
    today3 = cur4.fetchall()
    today4 = cur5.fetchall()
    today5 = cur6.fetchall()
    cur.close()
    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()
    cur6.close()
    db.close()
    print(today1)
    print(today2)
    print(today3)
    print(today4)
    print(today5)
    return render_template('hello.html', title='flask test', members=members,members1=members1,today1=today1,today2=today2,today3=today3,today4=today4,today5=today5) #変更

if __name__ == '__main__':
    app.run(debug=True, port=8085)