""" Ce code est le Point d’entrée de l’application Streamlit """

# Importation des libraries
import streamlit as st
from mongo_queries import get_top_movies
from neo4j_queries import get_top_actor

st.title("Projet NoSQL : Analyse de Films")

# Permet d'afficher les films les mieux notés
st.subheader("Films les mieux notés")
try:
    movies = get_top_movies(limit=5)
    for movie in movies:
        st.write(f"**{movie['title']}** - Note : {movie['rating']}")
except Exception as e:
    st.error(f"Erreur MongoDB : {e}")
    movies = []

# Permet d'afficher l'acteur le plus populaire
st.subheader("Acteur ayant joué dans le plus de films")
try:
    actor = get_top_actor()
    st.write(f"**{actor['name']}** avec {actor['nb_films']} films")
except Exception as e:
    st.error(f"Erreur Neo4j : {e}")
    actor = None

# Section DEBUG (facultatif mais utile)
st.subheader("DEBUG")
st.write("Movies:", movies)
st.write("Actor:", actor)
