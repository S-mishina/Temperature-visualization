#include "DHT.h" //ライブラリインクルード
#define DHT_Pin 8 //DHT11のDATAピンを定義
#define DHT_Type DHT11 //センサの型番定義　DHT11,DHT22など

DHT dht(DHT_Pin, DHT_Type); //センサ初期化
/* 計測値設定 */
float humidity = 0.0f; //湿度
float tempC = 0.0f; //摂氏温度
void setup() {
Serial.begin(9600); //シリアル通信のデータ転送レートを9600bpsで指定。bpsはビット/秒。
Serial.println("温度計測を始めます"); //画面に表示
dht.begin(); //温湿度センサー開始
}
void loop() {
delay(2000); //2秒待つ　データの読み出し周期1秒以上必要。
humidity = dht.readHumidity(); //湿度の読み出し
tempC = dht.readTemperature(); //温度の読み出し 摂氏
/* 読み取れたかどうかのチェック */
if (isnan(humidity) || isnan(tempC)) {
Serial.println("Read failure!");
return;
}
/* 以下読み取り値の表示 */
Serial.print("湿度: ");
Serial.print(humidity);
Serial.println("[%]");
Serial.print("温度: "); 
Serial.print(tempC);
Serial.println("[℃]");
}
//参考URL
//https://omoroya.com/arduino-lesson11/
