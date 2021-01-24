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
<img width="477" alt="スクリーンショット 2021-01-24 21 32 31" src="https://user-images.githubusercontent.com/45090872/105630312-cbf18400-5e8b-11eb-9a75-196ffc5915ad.png">

## 運用サーバとの連携(主に可視化部分)
現状の構成<br>
<img width="490" alt="スクリーンショット 2021-01-20 15 52 26" src="https://user-images.githubusercontent.com/45090872/105137974-92411600-5b37-11eb-83d3-caa25fb626fe.png">
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
### 現状対応している機能
・現在の気温の表示<br>
・日別の温度可視化（5日分）
## 画面UI（Flask）
<center>

</center>






