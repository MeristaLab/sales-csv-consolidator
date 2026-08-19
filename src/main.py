# python src/main.py

import sys
sys.path.append("src") # importの検索リスト
from pathlib import Path
from core.processor import run_and_save


input_dir = Path("samples/input")
output_path = Path("samples/output/統合売上データ.csv")
try:
    merged, success, error, total = run_and_save(input_dir, output_path)
    print(merged)
    print(f"成功:{success}/{total}")
    print(f"失敗:{error}/{total}")
    
except ValueError as e:
    print(f"エラー: {e}")