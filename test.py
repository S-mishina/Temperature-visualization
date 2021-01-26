import mysql.connector as mydb
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
cur = conn.cursor()
day="2021-01-17 18:22:42.454248"
time=" 18:22:42.454248"
s5=14.7
cur.execute("INSERT INTO `temperature` (`day`,`time`, `temperature`)"+ "VALUES"+ "("+"'"+str(day)+"'"+","+"'"+str(time)+"'"+","+str(s5)+")")
conn.commit()
cur.close()
conn.close()