# Temperature-visualization
・DH11センサを利用した温度可視化プログラム
## Arudino側のプログラム
・sensor.ino
## python側プログラム
・sensor.py
## sensor.pyの仕組み
①まずarudinoからセンサーのデータをシリアル通信で受信する.<br>
②受信したデータをmysqlに保存する.<br>
現状は上記のような設計になっている.




