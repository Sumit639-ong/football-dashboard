import streamlit as st
import sqlite3
import pandas as pd

# ---------------- TEAM LOGOS ----------------

team_logos = {

"Arsenal":"https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
"Aston Villa":"https://upload.wikimedia.org/wikipedia/en/f/f9/Aston_Villa_FC_crest.svg",
"Bournemouth":"https://upload.wikimedia.org/wikipedia/en/e/e5/AFC_Bournemouth_%282013%29.svg",
"Brentford":"https://upload.wikimedia.org/wikipedia/en/2/2a/Brentford_FC_crest.svg",
"Brighton":"https://upload.wikimedia.org/wikipedia/en/f/fd/Brighton_%26_Hove_Albion_logo.svg",
"Chelsea":"https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
"Crystal Palace":"https://upload.wikimedia.org/wikipedia/en/a/a2/Crystal_Palace_FC_logo_%282022%29.svg",
"Everton":"https://upload.wikimedia.org/wikipedia/en/7/7c/Everton_FC_logo.svg",
"Fulham":"https://upload.wikimedia.org/wikipedia/en/e/eb/Fulham_FC_%28shield%29.svg",
"Liverpool":"https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
"Luton Town":"https://upload.wikimedia.org/wikipedia/en/9/9d/Luton_Town_logo.svg",
"Manchester City":"https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
"Manchester United":"https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
"Newcastle":"https://upload.wikimedia.org/wikipedia/en/5/56/Newcastle_United_Logo.svg",
"Nottingham Forest":"https://upload.wikimedia.org/wikipedia/en/e/e5/Nottingham_Forest_F.C._logo.svg",
"Sheffield United":"https://upload.wikimedia.org/wikipedia/en/5/5f/Sheffield_United_FC_logo.svg",
"Tottenham":"https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg",
"West Ham":"https://upload.wikimedia.org/wikipedia/en/c/c2/West_Ham_United_FC_logo.svg",
"Wolves":"https://upload.wikimedia.org/wikipedia/en/f/fc/Wolverhampton_Wanderers.svg",
"Burnley":"https://upload.wikimedia.org/wikipedia/en/6/6d/Burnley_FC_Logo.svg"

}

# ---------------- DATABASE ----------------

conn = sqlite3.connect("test.db")

st.set_page_config(layout="wide")

# ---------------- CSS ----------------

st.markdown("""
<style>

.match-card {
    background-color: #0e1117;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #262730;
    margin-bottom: 10px;
}

.match-title {
    font-size:16px;
    font-weight:600;
    color:#ffffff;
}

.match-info {
    font-size:13px;
    color:#a0a0a0;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "selected_match" not in st.session_state:
    st.session_state.selected_match = None

# ---------------- SIDEBAR ----------------

page = st.sidebar.radio(
    "Select Page",
    ["Home","EPL","UCL","CARGO CUP","FA CUP","Add Match","Settings"]
)

if st.button("🔄 Refresh Dashboard"):
    st.rerun()

# ---------------- HOME PAGE ----------------

if page == "Home":

    st.title("⚽ Football Admin Dashboard")

    data = pd.read_sql("SELECT * FROM matches", conn)
    
    for index, row in data.iterrows():
        
        col1, col2, col3 = st.columns([1,4,1])

    with col1:
        logo1 = team_logos.get(row["team1"])
        if logo1:
            st.image(logo1, width=60)

    with col2:

        st.markdown(f"""
        <div class="match-card">

        <div class="match-title">
        {row['team1']} vs {row['team2']}
        </div>

        <div class="match-info">
        📅 {row['match_date']}
        </div>

        <div class="match-info">
        🏆 {row['league']}
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button("View Match", key=row["id"]):
            st.session_state.selected_match = row["id"]

    with col3:
        logo2 = team_logos.get(row["team2"])
        if logo2:
            st.image(logo2, width=60)

    st.divider()
    
# ---------------- EPL PAGE ----------------

if page == "EPL":

    st.title("🏆 EPL Matches")

    data = pd.read_sql("SELECT * FROM matches WHERE league='EPL'", conn)
    
    for index, row in data.iterrows():
        
        col1, col2, col3 = st.columns([6,1,1])

    with col1:
        st.markdown(f"### {row['team1']} ⚽ {row['team2']}")
        st.write(f"📅 {row['match_date']}")

    with col2:
        if st.button("✏️ Edit", key=f"edit_epl_{index}"):
            st.write("Edit match:", row['team1'], "vs", row['team2'])

    with col3:
        if st.button("🗑 Delete", key=f"delete_epl_{index}"):
            st.write("Delete match:", row['team1'], "vs", row['team2'])

    st.divider()

# ---------------- UCL PAGE ----------------

if page == "UCL":

    st.title("🏆 UCL Matches")

    data = pd.read_sql("SELECT * FROM matches WHERE league='UCL'", conn)
    
    for index, row in data.iterrows():
        
        col1, col2, col3 = st.columns([6,1,1])

    with col1:
        st.markdown(f"### {row['team1']} ⚽ {row['team2']}")
        st.write(f"📅 {row['match_date']}")

    with col2:
        if st.button("✏️ Edit", key=f"edit_epl_{index}"):
            st.write("Edit match:", row['team1'], "vs", row['team2'])

    with col3:
        if st.button("🗑 Delete", key=f"delete_epl_{index}"):
            st.write("Delete match:", row['team1'], "vs", row['team2'])

    st.divider()

# ---------------- CARGO CUP ----------------

if page == "CARGO CUP":

    st.title("🏆 CARGO CUP Matches")

    data = pd.read_sql("SELECT * FROM matches WHERE league='CARGO CUP'", conn)
    
    for index, row in data.iterrows():
        
        col1, col2, col3 = st.columns([6,1,1])

    with col1:
        st.markdown(f"### {row['team1']} ⚽ {row['team2']}")
        st.write(f"📅 {row['match_date']}")

    with col2:
        if st.button("✏️ Edit", key=f"edit_ucl_{index}"):
            st.write("Edit match:", row['team1'], "vs", row['team2'])

    with col3:
        if st.button("🗑 Delete", key=f"delete_ucl_{index}"):
            st.write("Delete match:", row['team1'], "vs", row['team2'])

    st.divider()

# ---------------- FA CUP PAGE --------------

if page == "FA CUP":

    st.title("🏆 FA CUP Matches")

    data = pd.read_sql("SELECT * FROM matches WHERE league='FA CUP'", conn)
    
    for index, row in data.iterrows():
        
        col1, col2, col3 = st.columns([6,1,1])

    with col1:
        st.markdown(f"### {row['team1']} ⚽ {row['team2']}")
        st.write(f"📅 {row['match_date']}")

    with col2:
        if st.button("✏️ Edit", key=f"edit_ucl_{index}"):
            st.write("Edit match:", row['team1'], "vs", row['team2'])

    with col3:
        if st.button("🗑 Delete", key=f"delete_ucl_{index}"):
            st.write("Delete match:", row['team1'], "vs", row['team2'])

    st.divider()


# ---------------- ADD MATCH ----------------

if page == "Add Match":

    st.title("➕ Add Match")

    league_input = st.selectbox(
        "League",
        ["EPL","UCL","CARGO CUP","FA CUP"]
    )

    team1 = st.text_input("Team 1")
    team2 = st.text_input("Team 2")
    date = st.text_input("Match Date")

    if st.button("Add Match"):

        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO matches (league,team1,team2,match_date) VALUES (?,?,?,?)",
        (league_input,team1,team2,date)
        )

        conn.commit()

        st.success("Match Added")

# ---------------- SETTINGS ----------------

if page == "Settings":

    st.title("⚙ Admin Settings")
    st.write("Admin Settings Panel")
    

# ---------------- MATCH DETAIL PAGE ----------------

if st.session_state.selected_match:

    match_id = st.session_state.selected_match

    match = pd.read_sql(
        f"SELECT * FROM matches WHERE id={match_id}",
        conn
    )

    row = match.iloc[0]

    st.title("⚽ Match Details")

    st.header(f"{row['team1']} vs {row['team2']}")

    st.write(f"📅 Date: {row['match_date']}")
    st.write(f"🏆 League: {row['league']}")
    st.write(f"🆔 Match ID: {row['id']}")

    if st.button("⬅ Back"):
        st.session_state.selected_match = None
