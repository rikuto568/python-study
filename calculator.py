# 簡単な電卓プログラム（初心者向け）

print("簡単な電卓プログラム")

# 数字を入力
a = float(input("1つ目の数字を入力してください："))
b = float(input("2つ目の数字を入力してください："))

# 計算方法を選ぶ
print("計算方法を選んでください")
print("1：足し算")
print("2：引き算")
print("3：掛け算")
print("4：割り算")

choice = input("番号を入力してください：")

# 計算と表示
if choice == "1":
    print("結果：", a + b)
elif choice == "2":
    print("結果：", a - b)
elif choice == "3":
    print("結果：", a * b)
elif choice == "4":
    if b == 0:
        print("エラー：0で割ることはできません")
    else:
        print("結果：", a / b)
else:
    print("正しい番号を入力してください")
