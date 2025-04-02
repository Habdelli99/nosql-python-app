""" Ce code est le Point d’entrée de l’application Streamlit """

# Importation des libraries
import streamlit as st
from app.mongo_queries import get_top_movies
from app.neo4j_queries import get_top_actor

st.title("Projet NoSQL : Analyse de Films")

# Permet d'afficher les films les mieux notés
st.subheader("Films les mieux notés")
movies = get_top_movies(limit=5)
for movie in movies:
    st.write(f"**{movie['title']}** - Note : {movie['rating']}")

# Permet d'afficher l'acteur le plus populaire
st.subheader("Acteur ayant joué dans le plus de films")
actor = get_top_actor()
st.write(f"**{actor['name']}** avec {actor['nb_films']} films")
