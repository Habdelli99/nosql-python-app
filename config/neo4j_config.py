""" Fichier de configuration des connexions Neo4j """

import os
from dotenv import load_dotenv

# Permet de Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Configuration Neo4j
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Options générales
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

if DEBUG:
    print(f"🔧 Mode DEBUG activé\nNeo4j: {NEO4J_URI}")
