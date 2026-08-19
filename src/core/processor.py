from pathlib import Path
import pandas as pd
from core.normalizer import rename_columns, normalize_dates,  drop_unnecessary_columns
from core.validator import check_required_columns,check_missing_values, check_numeric_columns, check_not_empty
from core.normalizer import rename_columns_to_japanese

# csvDataをDataFrameとして取り出す
def load_csv(path):
    return pd.read_csv(path)

# ファイル名から店舗名を取得
def extract_store_name(filename):
    return filename.split("_")[0]

# 1ファイル分を読込・検証・正規化し、店舗名を付与して返す
def process_one_file(path):
    store_name = extract_store_name(path.name)
    df = load_csv(path)
    check_not_empty(df)
    df = rename_columns(df)
    check_required_columns(df)
    df = normalize_dates(df)
    df = drop_unnecessary_columns(df)
    check_missing_values(df)
    check_numeric_columns(df)
    df["store"] = store_name
    return df

# フォルダ内の全CSVを処理し、エラーのあるファイルはスキップして1つに結合する
def process_all_files(input_dir):
    dfs = []
    error_count = 0
    total_count = 0
    for path in Path(input_dir).glob("*.csv"):
        total_count += 1
        try:
            df = process_one_file(path)
            dfs.append(df)
        except ValueError as e:
            error_count += 1
    if not dfs:
        raise ValueError("処理できるファイルがありませんでした")
    merged = pd.concat(dfs)
    merged = merged.sort_values("date")
    return merged, len(dfs), error_count, total_count

#フォルダ内CSVを統合し、日本語列名に変換してCSVに保存した上で結果を返す
def run_and_save(input_dir, output_path):
    merged, success, error, total = process_all_files(input_dir)
    merged = rename_columns_to_japanese(merged)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(output_path, index=False)
    return merged, success, error, total