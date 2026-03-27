import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

st.set_page_config(
    page_title="IPL Data Analyzer",
    page_icon="🏏",
    layout="wide"
)

def get_connection():
    return sqlite3.connect("database/ipl.db")

st.title("🏏 IPL Data Analyzer")
st.markdown("Analyzing **IPL matches from 2008 to 2024** using Python, Pandas, SQLite and Streamlit.")
st.divider()

st.sidebar.title("📊 Navigation")
analysis = st.sidebar.selectbox(
    "Select Analysis",
    ["Team Wins", "Top Batsmen", "Top Bowlers", "Top Venues", "Matches Per Season"]
)

if analysis == "Team Wins":
    st.header("🏆 Top 10 Teams by Match Wins")

    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT winner, COUNT(*) as total_wins
        FROM matches
        WHERE winner != ''
        GROUP BY winner
        ORDER BY total_wins DESC
        LIMIT 10
    """, conn)
    conn.close()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🥇 Most Wins", df.iloc[0]['winner'], f"{df.iloc[0]['total_wins']} wins")
    with col2:
        st.metric("🥈 Second", df.iloc[1]['winner'], f"{df.iloc[1]['total_wins']} wins")
    with col3:
        st.metric("🥉 Third", df.iloc[2]['winner'], f"{df.iloc[2]['total_wins']} wins")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df, x="winner", y="total_wins",
                hue="winner", palette="Blues_d", legend=False, ax=ax)
    ax.set_title("Top 10 Teams by Match Wins in IPL", fontsize=16)
    ax.set_xlabel("Team", fontsize=12)
    ax.set_ylabel("Total Wins", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    st.info("💡 Mumbai Indians lead with the most wins, followed closely by Chennai Super Kings.")

elif analysis == "Top Batsmen":
    st.header("🏏 Top 10 Run Scorers in IPL History")

    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT batter, SUM(batsman_runs) as total_runs
        FROM deliveries
        GROUP BY batter
        ORDER BY total_runs DESC
        LIMIT 10
    """, conn)
    conn.close()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🥇 Top Scorer", df.iloc[0]['batter'], f"{df.iloc[0]['total_runs']} runs")
    with col2:
        st.metric("🥈 Second", df.iloc[1]['batter'], f"{df.iloc[1]['total_runs']} runs")
    with col3:
        st.metric("🥉 Third", df.iloc[2]['batter'], f"{df.iloc[2]['total_runs']} runs")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x="total_runs", y="batter",
                hue="batter", palette="Oranges_d", legend=False, ax=ax)
    ax.set_title("Top 10 Run Scorers in IPL History", fontsize=16)
    ax.set_xlabel("Total Runs", fontsize=12)
    ax.set_ylabel("Batsman", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)

    st.info("💡 Virat Kohli leads with 8,014 runs — nearly 1,250 more than the second placed Shikhar Dhawan.")

elif analysis == "Top Bowlers":
    st.header("🎳 Top 10 Wicket Takers in IPL History")

    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT bowler, COUNT(*) as total_wickets
        FROM deliveries
        WHERE is_wicket = 1
        AND dismissal_kind NOT IN ('run out', 'retired hurt', 'obstructing the field')
        GROUP BY bowler
        ORDER BY total_wickets DESC
        LIMIT 10
    """, conn)
    conn.close()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🥇 Top Wicket Taker", df.iloc[0]['bowler'], f"{df.iloc[0]['total_wickets']} wickets")
    with col2:
        st.metric("🥈 Second", df.iloc[1]['bowler'], f"{df.iloc[1]['total_wickets']} wickets")
    with col3:
        st.metric("🥉 Third", df.iloc[2]['bowler'], f"{df.iloc[2]['total_wickets']} wickets")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x="total_wickets", y="bowler",
                hue="bowler", palette="Greens_d", legend=False, ax=ax)
    ax.set_title("Top 10 Wicket Takers in IPL History", fontsize=16)
    ax.set_xlabel("Total Wickets", fontsize=12)
    ax.set_ylabel("Bowler", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)

    st.info("💡 YS Chahal leads with 205 wickets, making him the most successful IPL bowler of all time.")

elif analysis == "Top Venues":
    st.header("🏟️ Top 10 Venues by Matches Hosted")

    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT venue, COUNT(*) as total_matches
        FROM matches
        GROUP BY venue
        ORDER BY total_matches DESC
        LIMIT 10
    """, conn)
    conn.close()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🥇 Most Matches", df.iloc[0]['venue'], f"{df.iloc[0]['total_matches']} matches")
    with col2:
        st.metric("🥈 Second", df.iloc[1]['venue'], f"{df.iloc[1]['total_matches']} matches")
    with col3:
        st.metric("🥉 Third", df.iloc[2]['venue'], f"{df.iloc[2]['total_matches']} matches")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df, x="total_matches", y="venue",
                hue="venue", palette="Purples_d", legend=False, ax=ax)
    ax.set_title("Top 10 Venues by Matches Hosted", fontsize=16)
    ax.set_xlabel("Total Matches", fontsize=12)
    ax.set_ylabel("Venue", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)

    st.info("💡 Eden Gardens in Kolkata has hosted the most IPL matches, followed by Wankhede Stadium in Mumbai.")

elif analysis == "Matches Per Season":
    st.header("📅 IPL Matches Played Per Season")

    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT season, COUNT(*) as total_matches
        FROM matches
        GROUP BY season
        ORDER BY season
    """, conn)
    conn.close()

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📆 Total Seasons", len(df))
    with col2:
        st.metric("📈 Most Matches", f"{df['total_matches'].max()} matches",
                  df.loc[df['total_matches'].idxmax(), 'season'])
    with col3:
        st.metric("📉 Least Matches", f"{df['total_matches'].min()} matches",
                  df.loc[df['total_matches'].idxmin(), 'season'])

    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x="season", y="total_matches",
                 marker="o", color="steelblue", ax=ax)
    ax.set_title("IPL Matches Played Per Season", fontsize=16)
    ax.set_xlabel("Season", fontsize=12)
    ax.set_ylabel("Total Matches", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    st.info("💡 IPL grew from 58 matches in 2007/08 to 74 matches in recent seasons. The 2014 dip was due to CSK and RR suspension.")

st.divider()
st.markdown("Built with ❤️ using Python · Pandas · SQLite · Matplotlib · Seaborn · Streamlit")