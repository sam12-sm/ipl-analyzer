import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ipl.db")

print("=== Q1: Most Match Wins ===")
q1="""
SELECT winner, COUNT(*) as total_wins
FROM matches
WHERE winner != ''
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 10
"""
df1 = pd.read_sql_query(q1, conn)
print(df1)
print()

print("=== Q2: Top 10 Run Scorers ===")
q2 = """
SELECT batter, SUM(batsman_runs) as total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10
"""
df2 = pd.read_sql_query(q2, conn)
print(df2)
print()

print("=== Q3: Top 10 Wicket Takers ===")
q3 = """
SELECT bowler, COUNT(*) as total_wickets
FROM deliveries
WHERE is_wicket = 1
AND dismissal_kind NOT IN ('run out', 'retired hurt', 'obstructing field')
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10
"""

df3 = pd.read_sql_query(q3, conn)
print(df3)
print()

print("=== Q4: Top Venues ===")
q4 = """
SELECT venue, COUNT(*) as total_matches
FROM matches
GROUP BY venue
ORDER BY total_matches DESC
LIMIT 10
"""

df4 = pd.read_sql_query(q4, conn)
print(df4)
print()

print("=== Q5: Matches Per Season ===")
q5 = """
SELECT season, COUNT(*) as total_matches
FROM matches
GROUP BY season
ORDER BY season
"""

df5 = pd.read_sql_query(q5, conn)
print(df5)

conn.close()