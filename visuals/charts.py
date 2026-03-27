import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

conn = sqlite3.connect("database/ipl.db")

sns.set_theme(style="whitegrid")

q1 = """
SELECT winner, COUNT(*) as total_wins
FROM matches
WHERE winner != ''
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 10
"""
df1 = pd.read_sql_query(q1, conn)

plt.figure(figsize=(12, 6))
sns.barplot(data=df1, x="winner", y="total_wins",
            hue="winner", palette="Blues_d", legend=False)
plt.title("Top 10 Teams by Match Wins in IPL", fontsize=16)
plt.xlabel("Team", fontsize=12)
plt.ylabel("Total Wins", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("visuals/team_wins.png")
plt.show()
print("Chart 1 saved!")

q2 = """
SELECT batter, SUM(batsman_runs) as total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10
"""
df2 = pd.read_sql_query(q2, conn)

plt.figure(figsize=(10, 6))
sns.barplot(data=df2, x="total_runs", y="batter",
            hue="batter", palette="Oranges_d", legend=False)
plt.title("Top 10 Run Scorers in IPL History", fontsize=16)
plt.xlabel("Total Runs", fontsize=12)
plt.ylabel("Batsman", fontsize=12)
plt.tight_layout()
plt.savefig("visuals/top_scorers.png")
plt.show()
print("Chart 2 saved!")

q3 = """
SELECT bowler, COUNT(*) as total_wickets
FROM deliveries
WHERE is_wicket = 1
AND dismissal_kind NOT IN ('run out', 'retired hurt', 'obstructing the field')
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10
"""
df3 = pd.read_sql_query(q3, conn)

plt.figure(figsize=(10, 6))
sns.barplot(data=df3, x="total_wickets", y="bowler",
            hue="bowler", palette="Greens_d", legend=False)
plt.title("Top 10 Wicket Takers in IPL History", fontsize=16)
plt.xlabel("Total Wickets", fontsize=12)
plt.ylabel("Bowler", fontsize=12)
plt.tight_layout()
plt.savefig("visuals/top_wickets.png")
plt.show()
print("Chart 3 saved!")

q4 = """
SELECT venue, COUNT(*) as total_matches
FROM matches
GROUP BY venue
ORDER BY total_matches DESC
LIMIT 10
"""
df4 = pd.read_sql_query(q4, conn)

plt.figure(figsize=(12, 6))
sns.barplot(data=df4, x="total_matches", y="venue",
            hue="venue", palette="Purples_d", legend=False)
plt.title("Top 10 Venues by Matches Hosted", fontsize=16)
plt.xlabel("Total Matches", fontsize=12)
plt.ylabel("Venue", fontsize=12)
plt.tight_layout()
plt.savefig("visuals/top_venues.png")
plt.show()
print("Chart 4 saved!")

q5 = """
SELECT season, COUNT(*) as total_matches
FROM matches
GROUP BY season
ORDER BY season
"""
df5 = pd.read_sql_query(q5, conn)

plt.figure(figsize=(12, 6))
sns.lineplot(data=df5, x="season", y="total_matches",
             marker="o", color="steelblue")
plt.title("IPL Matches Played Per Season", fontsize=16)
plt.xlabel("Season", fontsize=12)
plt.ylabel("Total Matches", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("visuals/matches_per_season.png")
plt.show()
print("Chart 5 saved!")

conn.close()
print("All charts saved successfully!")