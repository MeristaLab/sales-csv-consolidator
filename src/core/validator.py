import pandas as pd

REQUIRED_COLUMNS = ["date", "product", "price", "quantity"]

# 必須列チェック
def check_required_columns(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"必須列が不足しています: {missing}")

# 欠損チェック
def check_missing_values(df):
    missing_rows = df[df.isna().any(axis=1)]
    # df.isna(): 欠損値なら True, 値が入っていれば False
    # axis=0: 列ごとに, axis=1: 行ごとに
    if not missing_rows.empty: # miss行がなければOK
        raise ValueError(f"欠損値のある行があります:\n{missing_rows}")

# 数値異常チェック
def check_numeric_columns(df):
    numeric_cols = ["price", "quantity"]
    for col in numeric_cols:
        invalid = df[pd.to_numeric(df[col], errors="coerce").isna()]
        # 数値以外を検出
        if not invalid.empty:
            raise ValueError(f"{col}列に数値として読めない値があります:\n{invalid}")

# 空CSVチェック
def check_not_empty(df):
    if df.empty:
        raise ValueError("空のCSVです（データ行がありません）")