# 「」の中身を正規表現で抽出するプログラム（初心者向け）

import re

# 対象の文章
text = '今日は「Python」を勉強して、「正規表現」を使ってみた。'

# 正規表現で「」の中身を探す
results = re.findall('「(.*?)」', text)

# 結果を表示
print("抽出結果：")
for item in results:
    print(item)
