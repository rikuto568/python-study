#摂氏から華氏、華氏から摂氏へ変換するプログラム

# 摂氏 → 華氏に変換する関数
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


# 華氏 → 摂氏に変換する関数
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


print("温度変換プログラム")
print("1：摂氏 → 華氏")
print("2：華氏 → 摂氏")

choice = input("番号を入力してください（1 または 2）：")

if choice == "1":
    c = float(input("摂氏（℃）を入力してください："))
    result = celsius_to_fahrenheit(c)
    print("華氏（℉）は", result, "です")

elif choice == "2":
    f = float(input("華氏（℉）を入力してください："))
    result = fahrenheit_to_celsius(f)
    print("摂氏（℃）は", result, "です")

else:
    print("1 か 2 を入力してください")
