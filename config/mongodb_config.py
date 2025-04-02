""" Fichier de configuration des connexions MongoDB """

import os
from dotenv import load_dotenv

# Permet de Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Configuration MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "entertainment")

# Options générales
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

if DEBUG:
    print(f"🔧 Mode DEBUG activé\nMongoDB: {MONGO_URI}")
