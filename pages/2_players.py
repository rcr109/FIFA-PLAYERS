import streamlit as st

st.set_page_config(
    page_title="FIFA 2023 DATASET",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

df_data = st.session_state["data"]
clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione o clube", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Selecione o jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"], width=100)
st.title(player_stats["Name"])
st.markdown(f"**Clube:**  {player_stats['Club']}")
st.markdown(f"**Posição:**  {player_stats['Position']}")    

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"**Idade:**  {player_stats['Age']}")
with col2:
    st.markdown(f"**Altura:**  {player_stats['Height(cm.)'] / 100}")
with col3:  
    st.markdown(f"**Peso:**  {player_stats['Weight(lbs.)'] * 0.453:.2f}")     
with col4:  
    st.markdown(f"**Salário:**  £{player_stats['Wage(£)']}")

st.divider()

st.subheader(f"Overall {player_stats['Overall']}")

st.progress(player_stats["Overall"] / 100)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Passe", f"{player_stats["Value(£)"]:,.2f}")