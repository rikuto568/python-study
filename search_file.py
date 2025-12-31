import os

# ===== 設定 =====
search_dir = "."      # 検索したいフォルダ（"." は今いるフォルダ）
keyword = "bmi"      # 探したい文字列（例: "py", "report" など）
# =================

print(f"「{keyword}」を含むファイルを検索中...\n")

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if keyword in file:
            full_path = os.path.join(root, file)
            print(full_path)

print("\n検索完了")

