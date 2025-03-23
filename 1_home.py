import streamlit as st
import webbrowser
import pandas as pd
import datetime

st.set_page_config(
    page_title="FIFA 2023 DATASET",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "data" not in st.session_state:
    df_data = pd.read_csv("arquivos/dados/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.datetime.now().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state.data = df_data

st.markdown("# FIFA 2023 DATASET")
st.sidebar.markdown("Desenvolvido por: rcr109")
btn = st.button("Clique aqui para ver os dados")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
'''
O Football Player Dataset de 2017 a 2023 fornece informações abrangentes sobre jogadores profissionais de futebol. 
O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, 
estatísticas de jogo, detalhes do contrato e afiliações ao clube. 

Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas, pesquisadores e entusiastas
do futebol interessados ​​em explorar vários aspectos do mundo do futebol, pois permite estudar atributos do jogador, 
métricas de desempenho, avaliação de mercado, análise do clube, posicionamento do jogador e desenvolvimento do jogador 
ao longo do tempo.
'''
)