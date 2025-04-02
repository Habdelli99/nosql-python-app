""" Ce code permet les Fonctions utilitaires """

import pandas as pd

def format_results(results):
    """
    Permet de Convertir une liste de dictionnaires en DataFrame Pandas.
    
    :param results: Liste de dictionnaires
    :return: DataFrame Pandas
    """
    return pd.DataFrame(results)
