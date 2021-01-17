# Temperature-visualization
・DH11センサを利用した温度可視化プログラム
## Arudino側のプログラム
・sensor.ino
## python側プログラム
・sensor.py...シリアルモニタ-<br>
・server.py...falsk可視化システム
## sensor.pyの仕組み
①まずarudinoからセンサーのデータをシリアル通信で受信する.<br>
②受信したデータをmysqlに保存する.<br>
## server.py
flaskを利用したweb画面での可視化をする為のプログラム<br>
現状は取得時の日付,時間とその時の温度を可視化するところまでを可視化している.
## 画面UI
<img width="578" alt="スクリーンショット 2021-01-18 3 41 00" src="https://user-images.githubusercontent.com/45090872/104852546-fd73c800-593e-11eb-833a-a9056c66e775.png">






