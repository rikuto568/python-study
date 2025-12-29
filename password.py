import random
import string
#文字列をリストみたいに格納して、それをモジュールとして使用できる

print("パスワード生成プログラム")

length = int(input("パスワードの長さを入力してください："))

# 使う文字の集合（英大文字・英小文字・数字・記号）
characters = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(characters)

print("生成されたパスワード：")
print(password)
