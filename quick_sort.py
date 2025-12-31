def quick_sort(numbers):
    # 要素が1個以下なら、そのまま返す（並び替え不要）
    if len(numbers) <= 1:
        return numbers

    # 真ん中の要素をピボット（基準）にする
    pivot = numbers[len(numbers) // 2]

    # ピボットより小さいもの
    left = [x for x in numbers if x < pivot]

    # ピボットと同じもの
    middle = [x for x in numbers if x == pivot]

    # ピボットより大きいもの
    right = [x for x in numbers if x > pivot]

    # 左・真ん中・右をつなげる
    return quick_sort(left) + middle + quick_sort(right)


# ===== 実行部分 =====
data = [5, 3, 8, 4, 2, 7, 1, 6]

print("並び替え前:", data)
sorted_data = quick_sort(data)
print("並び替え後:", sorted_data)
