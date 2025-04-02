""" Ce code permet les Interactions avec MongoDB """

from pymongo import MongoClient

# Permet la Connexion à la base MongoDB
client = MongoClient("mongodb+srv://username:password@cluster.mongodb.net/")
db = client.entertainment

def get_top_movies(limit=5):
    """
    Permet de Récupèrer les films les mieux notés.
    
    :param limit: Nombre de films à récupérer
    :return: Liste des films
    """
    return list(db.films.find().sort("rating", -1).limit(limit))

def get_movie_by_title(title):
    """
    Permet de Rechercher un film par son titre.
    
    :param title: Titre du film
    :return: Dictionnaire du film
    """
    return db.films.find_one({"title": title})
