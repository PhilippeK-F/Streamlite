import streamlit as st

# Titre de l'application
st.title("Bienvenue sur le site web de :")
st.header("Philippe")

# Lien vers le dataset
st.markdown("[Lien vers le dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv)")

# Dictionnaire des villes et leurs images
villes_images = {
    'Manhattan': r"C:\Users\phili\Documents\Wild School\2025\Streamlite\manhattan.jpg",
    'Bronx': r"C:\Users\phili\Documents\Wild School\2025\Streamlite\bronx.jpg",
    'Queens': r"C:\Users\phili\Documents\Wild School\2025\Streamlite\queens.jpg",
    'Nan': r"C:\Users\phili\Documents\Wild School\2025\Streamlite\nan.jpg",
}

# Widget de sélection multiple
ville_selectionnee = st.selectbox("Choisissez une ville", list(villes_images.keys()))

# Affichage du texte et de l'image correspondants
if ville_selectionnee:
    st.write(f"Vous avez sélectionné : {ville_selectionnee}")
    st.image(villes_images[ville_selectionnee], caption=ville_selectionnee, use_container_width=True)