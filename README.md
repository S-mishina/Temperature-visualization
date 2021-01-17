# Temperature-visualization
・DH11センサを利用した温度可視化プログラム<br>
真面目にスイッチボット温度計システムに似せて作っています.<br>
## 今後の追加機能の予定
・アラート機能<br>
※LINEAPIの利用<br>
・レポート機能<br>
※LINEAPIの利用<br>
・Alexaアプリとの連携<br>
## 回路図について
（今後掲載）
## ラズパイとの連携
(今後検討)
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
## 画面UI（Flask）
<center>
<img width="578" alt="スクリーンショット 2021-01-18 3 41 00" src="https://user-images.githubusercontent.com/45090872/104852546-fd73c800-593e-11eb-833a-a9056c66e775.png">
</center>






