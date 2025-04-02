""" Ce code permet la Visualisation des données avec Streamlit et Matplotlib/Plotly """

# Importation des librairies
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from app.mongo_queries import get_top_movies
from app.neo4j_queries import get_top_actor

st.title("Visualisation des Données NoSQL")

# Permet de Récupérer les films les mieux notés
st.subheader("Distribution des Notes de Films")

movies = get_top_movies(limit=10)
if movies:
    df_movies = pd.DataFrame(movies)
    
    # Permet de voir l'Histogramme des notes
    fig, ax = plt.subplots()
    sns.histplot(df_movies['rating'], bins=10, kde=True, ax=ax)
    ax.set_xlabel("Note du Film")
    ax.set_ylabel("Nombre de Films")
    ax.set_title("Répartition des Notes des Films")
    
    st.pyplot(fig)
else:
    st.write("Aucun film trouvé.")

# Permet de Récupérer l'acteur ayant joué dans le plus de films
st.subheader("Acteur avec le plus grand nombre de films")

actor = get_top_actor()
if actor:
    st.write(f"**{actor['name']}** a joué dans **{actor['nb_films']}** films.")
else:
    st.write("Aucun acteur trouvé.")
