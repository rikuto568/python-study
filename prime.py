print("素数判定プログラム")

n = int(input("正の整数を入力してください："))

if n <= 1:
    print("素数ではありません")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("素数です")
    #スイッチみたいな感じ
    else:
        print("素数ではありません")
