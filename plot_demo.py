import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Data Manipulation and Visualization", layout="wide")
st.title("Data Manipulation and Visualization")
st.markdown("![Streamlit](https://res.cloudinary.com/dyd911kmh/image/upload/v1640050215/image27_frqkzv.png)")
st.markdown("[liens vers la doc ](https://docs.streamlit.io/)")
st.markdown("""Sommaire :
1. File import
---
2. Filter data
---
3. Histogram
---
4. Chart
---
""")

st.subheader("File import")
file = st.file_uploader("Choose a file")
if file is not None:
        df = pd.read_csv(file)
        st.write(df.head())
        st.subheader("Filter data")
        selected_column = st.selectbox("Column",df.columns)
        input = st.text_input("Value filter")
        filtered_df = df[df[selected_column]==input]
        st.write(filtered_df)

        st.subheader("Histogram")
        col1, col2 = st.columns(2)
        with col1:
                bins = st.slider("Number of bars",min_value = 1, max_value = 200 )
        with col2:
                x_axis = st.selectbox("x axis", df.columns)
                fig,ax = plt.subplots()
                ax.hist(df[x_axis], bins)
                st.pyplot(fig)

        st.subheader("Chart")
        graph_type = st.selectbox("graph type",["Ligne", "Barre", "Nuage de points"])

        col1, col2 = st.columns(2)
        with col1:
                x_axis = st.selectbox("x axis",df.columns,key="x axis line")
        with col2:
                y_axis = st.selectbox("y axis",df.columns,key="y axis line")
        fig,ax = plt.subplots()
                
        if graph_type == "Ligne":
                ax.plot(x_axis, y_axis, data = df)
        if graph_type == "Barre":
                ax.bar(x_axis, y_axis, data = df)
        if graph_type == "Nuage de points":
                ax.scatter(x_axis, y_axis, data = df)

        ax.set(xlabel = x_axis, ylabel = y_axis)
        st.pyplot(fig)
                

# Les widgets Streamlit exécutent automatiquement le script
# de haut en bas. Comme ce bouton n'est connecté à aucune
# autre logique, il ne fait que renvoyer un résultat vide.

st.button("Re-run")