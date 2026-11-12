from pathlib import Path
import sqlite3
import pandas as pd

DB_PATH = Path("data/processed/bank.db")
SQL_DIR = Path("sql")
OUT_DIR = Path("outputs")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    for sql_file in sorted(SQL_DIR.glob("*.sql")):
        df = pd.read_sql(sql_file.read_text(), conn)
        df.to_csv(OUT_DIR / f"{sql_file.stem}.csv", index=False)
        print(f"{sql_file.name}: {len(df)} rows")
    conn.close()


if __name__ == "__main__":
    main()