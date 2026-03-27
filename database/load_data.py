import pandas as pd
import sqlite3

matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

matches['venue'] = matches['venue'].replace({
    'Wankhede Stadium, Mumbai': 'Wankhede Stadium'
})

conn = sqlite3.connect("database/ipl.db")

matches.to_sql("matches", conn, if_exists="replace", index = False)
deliveries.to_sql("deliveries", conn, if_exists="replace", index = False)

print(f"matches table: {len(matches)} rows loaded")
print(f"deliveries table: {len(deliveries)} rows loaded")

conn.close()
print("databse created successfully")
