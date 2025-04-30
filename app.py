import streamlit as st
import requests
import random
# Config
API_KEY = "SUA_CHAVE_API_NINJAS"
HEADERS = {"X-Api-Key": API_KEY}
GENRES = ["action", "comedy", "drama", "fantasy", "horror"]

# Fundo aleatório
colors = ['#FFCDD2', '#F8BBD0', '#E1BEE7', '#BBDEFB', '#C8E6C9']
st.markdown(f"<style>body {{ background-color: {random.choice(colors)}; }}</style>", unsafe_allow_html=True)

# Função para obter filme
def get_random_movie():
    genre = random.choice(GENRES)
    response = requests.get(f"https://api.api-ninjas.com/v1/movies?genre={genre}", headers=HEADERS)
    if response.ok:
        movie = random.choice(response.json())
        return movie
    return None

# Traduzir texto
def traduzir(texto):
    return GoogleTranslator(source='auto', target='pt').translate(texto)

# Interface
st.title("🎬 CineSurpresa")
if st.button("🎲 Surpreenda-me!"):
    filme = get_random_movie()
    if filme:
        titulo_pt = traduzir(filme['title'])
        sinopse_pt = traduzir(filme['description'])
        st.subheader(f"🎞️ {titulo_pt} ({filme['year']})")
        st.markdown(f"**Gênero:** {filme['genre'].capitalize()} | **Classificação:** {filme['rating']}")
        st.write(f"📝 {sinopse_pt}")
        if st.toggle("Mostrar original"):
            st.markdown(f"**Título Original:** {filme['title']}")
            st.markdown(f"**Descrição Original:** {filme['description']}")
   
