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

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.title(f"Elenco do {club}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format="£%d", min_value=0, max_value=df_filtered["Wage(£)"].max()
                ),
                "Photo": st.column_config.ImageColumn("Photo"),
                "Flag": st.column_config.ImageColumn("Flag"),

             })
             
             
             