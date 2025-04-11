""" Ce code permet les Interactions avec Neo4j """

from neo4j import GraphDatabase

# Permet la Connexion à Neo4j
driver = GraphDatabase.driver("neo4j+s://7835be7a.databases.neo4j.io", auth=("neo4j", "EBn4PEizlekWio5mBYM3A4u-aJSmpyLvwcxKxTzDJNw"))

def get_top_actor():
    """
    Permet de Trouver l'acteur ayant joué dans le plus de films.
    
    :return: Dictionnaire avec le nom et le nombre de films
    """
    with driver.session() as session:
        result = session.run("""
            MATCH (a:Actor)-[:A_JOUE]->(m:Movie)
            RETURN a.name AS name, COUNT(m) AS nb_films
            ORDER BY nb_films DESC LIMIT 1
        """)
        return result.single()
