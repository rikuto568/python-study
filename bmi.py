# BMI計算プログラム（初心者向け）

print("BMI計算プログラムへようこそ")

# 身長と体重を入力
height = float(input("身長をメートルで入力してください（例：1.70）："))
weight = float(input("体重をキログラムで入力してください（例：60）："))

# BMIを計算
bmi = weight / (height * height)

# 結果を表示
print("あなたのBMIは", round(bmi, 2), "です")

# 判定
if bmi < 18.5:
    print("判定：やせ型")
elif bmi < 25:
    print("判定：標準")
elif bmi < 30:
    print("判定：肥満（1度）")
else:
    print("判定：肥満（2度以上）")
