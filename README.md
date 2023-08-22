# 月齢ドーナツ
月齢ドーナツは、ミニドーナツに指定した月齢の形のデコレーションを施すための装置です。

※画像をクリックでyoutube動画再生します  
[![月齢ドーナツ](https://github.com/airpocket-soundman/moon_donuts/blob/main/image/thumbnail.png)](https://www.youtube.com/watch?v=IT8nSHDabr0)

# 使い方
1.ミニドーナツを皿の上に載せます。  
2.microbitのAボタンとBボタンで、作りたい月齢を選びます。  
3.タッチセンサーを触ってカバーを動かします。  
4.カバーの上からパウダーシュガーをふるいかけます。  
5.もう一度タッチセンサーを触るとカバーが外れるためドーナツを取り出します。  

# 部品
micro:bit V2 1台  
USBバッテリー 1台  
[micro:bit用ワークショップモジュール](https://www.switch-science.com/products/5489) 1台  
LEGOテクニック歯車（大） 2個  
フレーム用LEGOテクニック 適量  
[GeekServo 9G Servo-Gray](https://www.switch-science.com/products/6811) 1台  
3Dプリンタパーツ 一式  
φ1しんちゅう線10cm  

# 3Dプリンターパーツ
準備中

# プログラム
開発は[micropython](https://python.microbit.org/v/3/)で行いました。
[/src](https://github.com/airpocket-soundman/moon_donuts/tree/main/src)に保存している「月齢ドーナツ_02.hex」をダウンロードするか、以下のコードを打ち込んで書き込むと動作します。

```python
# Imports go at the top
from microbit import *
a = 0
flag = 0
kakudo = [107,104,100, 97, 93,
           90, 86, 83, 77, 72,
           68, 63, 59, 54, 50,
           54, 59, 63, 68, 72,
           77, 83, 86, 90, 93,
           97,100,104]
pin0.write_analog(40)
# Code in a 'while True:' loop repeats forever
def sabo():
    display.scroll(kakudo[a])
    pin0.write_analog(kakudo[a])

while True:
    if pin_logo.is_touched():
        if flag == 0:
            sabo()
            sleep(1000)
            flag = 1
        elif flag == 1:
            pin0.write_analog(40)
            sleep(1000)
            flag = 0
    if button_a.is_pressed():
        a -= 1
        if a < 0:
            a = 0
        display.scroll(a)
    if button_b.is_pressed():
        a += 1
        if a > 28:
            a = 28
        display.scroll(a)

```


