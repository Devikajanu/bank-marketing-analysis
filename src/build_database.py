from pathlib import Path
import sqlite3
import pandas as pd

RAW_FILE = Path("data/raw/bank-additional-full.csv")
DB_PATH = Path("data/processed/bank.db")


def load_and_clean():
    df = pd.read_csv(RAW_FILE, sep=";")

    # 1. Rename columns: no dots, no SQL reserved words
    df = df.rename(columns={
        "emp.var.rate": "emp_var_rate",
        "cons.price.idx": "cons_price_idx",
        "cons.conf.idx": "cons_conf_idx",
        "nr.employed": "nr_employed",
        "default": "credit_default",
        "y": "subscribed",
    })

    # 2. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 3. Turn the target into 1/0
    df["subscribed"] = df["subscribed"].map({"yes": 1, "no": 0})

    # 4. Group ages
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 24, 34, 44, 54, 64, 120],
        labels=["<25", "25-34", "35-44", "45-54", "55-64", "65+"],
    ).astype(str)

    # 5. Flag customers contacted in an earlier campaign
    df["contacted_before"] = (df["pdays"] != 999).astype(int)

    return df


def main():
    df = load_and_clean()
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("bank_marketing", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Saved {len(df):,} rows to {DB_PATH}")


if __name__ == "__main__":
    main()