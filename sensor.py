import serial
import time
import datetime
import mysql.connector as mydb
ser = serial.Serial('/dev/tty.usbmodem14101', 9600)
conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='root',#ユーザidの記入
        password='',#パスワードの記入
        database='temperature'#データベースの名前を記入
    )
# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)
# 接続できているかどうか確認
print(conn.is_connected())
while (1):
    s=str(ser.readline())
    s1=s.replace("b'", '')
    s2=s1.replace("r", '')
    s3=s2.replace("n", '')
    s4=s3.replace("\\", '')
    s5=s4.replace("'", '')
    day = datetime.date.today()
    time1 = datetime.datetime.now()
    time2=str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second)
    print("現在時刻:"+str(s))
    print(str(s5)+"°")
    # コネクションが切れた時に再接続してくれるよう設定
    conn.ping(reconnect=True)
    # 接続できているかどうか確認
    print(conn.is_connected())
    cur = conn.cursor()
    cur.execute("INSERT INTO `temperature` (`day`,`time`, `temperature`)"+ "VALUES"+ "("+"'"+str(day)+"'"+","+"'"+str(time2)+"'"+","+str(s5)+")")
    conn.commit()
    cur.close()
    conn.close()
    time.sleep(0.2)

