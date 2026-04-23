Streamlit — Explorateur de quartiers de New York

Description du projet :

Application web interactive développée avec Streamlit (Python), permettant d'explorer les quartiers de New York à travers une interface de sélection visuelle.
Le projet s'appuie sur le dataset Taxis de New York (Seaborn) et propose une navigation par quartier avec affichage d'images.

Fonctionnalités :

- Titre et en-tête personnalisés
- Lien direct vers le dataset Taxis NYC (Seaborn)
- Selectbox interactive pour choisir un quartier de New York
- Affichage dynamique de l'image correspondante au quartier sélectionné
- Interface responsive via Streamlit

Dataset utilisé :

- Taxis NYC — Seaborn
- https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv
- Contient des données de courses de taxi à New York, incluant les quartiers de prise en charge et de dépôt.

Stack technique :

Outil, Usage, PythonLangage, Framework web interactif, Seaborn dataSource du dataset NYC Taxis.

Installation et lancement :

Clone le repo :

bashgit clone https://github.com/TON_USERNAME/Streamlite.git
cd Streamlite

Installe les dépendances :

- bashpip install streamlit

Lance l'application :

- bashstreamlit run app.py

Accède à l'app dans ton navigateur :

http://localhost:8501

Correction des chemins d'images

⚠️ Les chemins d'images dans le code original sont en chemin absolu Windows.
Pour que le projet fonctionne sur toute machine, remplace dans app.py :

python# Avant (chemin absolu Windows)
'Manhattan': r"C:\Users\phili\Documents\...\manhattan.jpg"

# Après (chemin relatif)
'Manhattan': 'manhattan.jpg'
Version corrigée de app.py :
pythonimport streamlit as st

st.title("Bienvenue sur le site web de :")
st.header("Philippe")

st.markdown("[Lien vers le dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv)")

villes_images = {
    'Manhattan': 'manhattan.jpg',
    'Bronx': 'bronx.jpg',
    'Queens': 'queens.jpg',
    'Nan': 'nan.jpg',
}

ville_selectionnee = st.selectbox("Choisissez une ville", list(villes_images.keys()))

if ville_selectionnee:
    st.write(f"Vous avez sélectionné : {ville_selectionnee}")
    st.image(villes_images[ville_selectionnee], caption=ville_selectionnee, use_container_width=True)

Auteur :
Philippe Kirstetter-Fender
Projet personnel — initiation à Streamlit (Python)
