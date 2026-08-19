
import pandas as pd

COLUMN_NAME_MAP = {
    "売上日": "date",
    "日付": "date",
    "販売日": "date",
    "商品名": "product",
    "商品": "product",
    "品名": "product",
    "単価": "price",
    "価格": "price",
    "金額": "price",
    "数量": "quantity",
    "個数": "quantity",
    "販売数": "quantity",
}

JAPANESE_COLUMN_MAP = {
    "date": "売上日",
    "product": "商品名",
    "price": "単価",
    "quantity": "数量",
    "store": "店舗名",
}

# 支店ごとに違う列名を共通名（date, product, price, quantityなど）に統一
def rename_columns(df):
    return df.rename(columns=COLUMN_NAME_MAP)

# バラバラな日付形式を統一
def normalize_dates(df):
    df["date"] = pd.to_datetime(df["date"])
    return df

# 「備考」のような不要列を削除
def drop_unnecessary_columns(df):
    return df[["date", "product", "price", "quantity"]]

# 列名を日本語に整形
def rename_columns_to_japanese(df):
    return df.rename(columns=JAPANESE_COLUMN_MAP)