# NoSQL Python App

Ce projet a été réalisé dans le cadre du module *NoSQL Databases*. Il permet de se connecter à des bases MongoDB et Neo4j dans le cloud, d'effectuer des requêtes, et de visualiser les résultats dans une interface interactive avec Streamlit.

### Fonctionnalités

1. Connexion à MongoDB et Neo4j dans le cloud.
2. Effectuer des opérations (Créer, Lire, Mettre à jour, Supprimer) sur MongoDB.
3. Interroger Neo4j à l'aide de Cypher pour créer des nœuds et des relations.
4. Visualisation des résultats avec des bibliothèques Python comme `matplotlib` et `seaborn` pour MongoDB, et `Neovis.js` pour Neo4j.

---

## Prérequis

Avant d'exécuter l'application, assurez-vous d'avoir les prérequis suivants installés :

- Python 3.8 ou supérieur
- MongoDB (si vous utilisez une base de données locale) ou MongoDB Atlas (si vous utilisez le cloud)
- Neo4j (si vous utilisez une base de données locale) ou Neo4j Aura (si vous utilisez le cloud)

---

## Technologies utilisées

- Python 3.x
- Streamlit
- MongoDB (via pymongo)
- Neo4j (via neo4j-driver)
- Matplotlib / Seaborn / Neovis.js
  
## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/Habdelli99/nosql-python-app.git
   
## Lancer le projet

```bash
pip install -r requirements.txt
streamlit run src/main.py
