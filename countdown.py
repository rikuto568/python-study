# カウントダウンタイマー（初心者向け）

import time

print("カウントダウンタイマー")
seconds = int(input("何秒カウントダウンしますか？："))

while seconds > 0:
    print("残り", seconds, "秒")
    time.sleep(1)   # 1秒停止させる関数
    
    seconds -= 1

print("時間になりました！")
