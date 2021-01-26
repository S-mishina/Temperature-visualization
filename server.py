from flask import Flask, render_template #追加
import pymysql #追加
import time
import datetime
from flask import render_template, url_for
from flask import request
import numpy 
import json
from dateutil.relativedelta import relativedelta


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
    return render_template('hello.html', title='トップページ', members=members,members1=members1,today1=today1,today2=today2,today3=today3,today4=today4,today5=today5) 

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
    return render_template('hello.html', title='日別部屋の温度可視化', members=members,members1=members1,today1=today1,today2=today2,today3=today3,today4=today4,today5=today5) #変更

@app.route('/hello1.html')
def hello2():
    #db setting
    db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            db='temperature',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    now = datetime.datetime.now()
    now1=now - datetime.timedelta(hours=1)
    now4=now - datetime.timedelta(hours=2)
    now6=now - datetime.timedelta(hours=3)
    now8=now - datetime.timedelta(hours=4)
    now3=now1.strftime('%H')#20
    now2=now4.strftime('%H')#19
    now5=now6.strftime('%H')#18
    now7=now8.strftime('%H')#17
    day = datetime.date.today()
    cur = db.cursor()
    cur1 = db.cursor()
    cur2 = db.cursor()
    cur3 = db.cursor()
    cur4 = db.cursor()
    t1day="SELECT * FROM `temperature` WHERE `day`="+"'"+str(day)+"'" +"ORDER BY `time` DESC LIMIT 1"
    t1day1="select avg(temperature) as temperature from temperature WHERE day="+"'"+str(day)+"'"+ "and time>="+"'"+str(now2)+":00:00"+"'"+" and time<="+"'"+str(now3)+":00:00"+"'"+";"
    t1day2="select avg(temperature) as temperature from temperature WHERE day="+"'"+str(day)+"'"+ "and time>="+"'"+str(now5)+":00:00"+"'"+" and time<="+"'"+str(now2)+":00:00"+"'"+";"
    t1day3="select avg(temperature) as temperature from temperature WHERE day="+"'"+str(day)+"'"+ "and time>="+"'"+str(now7)+":00:00"+"'"+" and time<="+"'"+str(now5)+":00:00"+"'"+";"
    t1day4="select avg(temperature) as temperature from temperature WHERE day="+"'"+str(day)+"'"+ "and time>="+"'"+str(now7)+":00:00"+"'"+" and time<="+"'"+str(now5)+":00:00"+"'"+";"
    cur.execute(t1day)
    cur1.execute(t1day1)
    cur2.execute(t1day2)
    cur3.execute(t1day3)
    cur4.execute(t1day4)
    
    test1 = cur1.fetchall()
    test2 = cur2.fetchall()
    test3 = cur3.fetchall()
    test4 = cur3.fetchall()
    test5 = cur.fetchall()

    cur.close()
    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()
    db.close()
    print(t1day1)
    print(test1)
    print(t1day2)
    print(test2)
    print(t1day3)
    print(t1day4)
    return render_template('hello1.html', title='時別部屋の温度可視化', test1=test1,test2=test2,test3=test3,test4=test4,test5=test5)
@app.route('/hello3.html')
def hello3():
    #db setting
    db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            db='temperature',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    now = datetime.datetime.now()
    now1=now - relativedelta(months=1)
    now4=now - relativedelta(months=2)
    now6=now - relativedelta(months=3)
    now8=now - relativedelta(months=4)
    now=now.strftime('%Y-%m')#1
    now3=now1.strftime('%Y-%m')#01
    now2=now4.strftime('%Y-%m')#11
    now5=now6.strftime('%Y-%m')#12
    now7=now8.strftime('%Y-%m')#10
    cur = db.cursor()
    cur1 = db.cursor()
    cur2 = db.cursor()
    cur3 = db.cursor()
    cur4 = db.cursor()
    cur5 = db.cursor()
    t1day5="select avg(temperature) as temperature from temperature WHERE day>="+"'"+str(now)+"-01"+"'"+" and day<="+"'"+str(now)+"-31"+"'"+";"
    t1day4="select avg(temperature) as temperature from temperature WHERE day>="+"'"+str(now3)+"-01"+"'"+" and day<="+"'"+str(now3)+"-31"+"'"+";"
    t1day3="select avg(temperature) as temperature from temperature WHERE day>="+"'"+str(now2)+"-01"+"'"+" and day<="+"'"+str(now2)+"-31"+"'"+";"
    t1day2="select avg(temperature) as temperature from temperature WHERE day>="+"'"+str(now5)+"-01"+"'"+" and day<="+"'"+str(now5)+"-31"+"'"+";"
    t1day1="select avg(temperature) as temperature from temperature WHERE day>="+"'"+str(now7)+"-01"+"'"+" and day<="+"'"+str(now7)+"-31"+"'"+";"
    cur1.execute(t1day1)
    cur2.execute(t1day2)
    cur3.execute(t1day3)
    cur4.execute(t1day4)
    cur5.execute(t1day5)
    cur.execute(t1day1)
    test1 = cur.fetchall()
    test5 = cur1.fetchall()
    test2 = cur2.fetchall()
    test3 = cur3.fetchall()
    test4 = cur4.fetchall()
    test5 = cur5.fetchall()
    cur.close()
    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()
    db.close()
    print(test5)
    print(test4)
    print(test3)
    print(test2)
    print(test1)
    return render_template('hello3.html', title='月別部屋の温度可視化',test5=test5,test1=test1,test2=test2,test3=test3,test4=test4)
if __name__ == '__main__':
    app.run(debug=True, port=8085)