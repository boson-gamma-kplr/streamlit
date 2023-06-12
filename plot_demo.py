import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import scipy
import pydeck as pdk

st.set_page_config(
    page_title="Data Manipulation and Visualization", layout="wide")
st.title("Data Manipulation and Visualization")
st.markdown(
    "![Streamlit](https://res.cloudinary.com/dyd911kmh/image/upload/v1640050215/image27_frqkzv.png)")
st.markdown("[liens vers la doc](https://docs.streamlit.io/)")
st.markdown("[Cheat sheet](https://docs.streamlit.io/library/cheatsheet)")
st.markdown("""Sommaire :
1. File import
---
2. Filter data
---
3. Histogram
---
4. Chart
---
5. Line chart
---
6. Area chart
""")

st.subheader("File import")
file = st.file_uploader("Choose a file")
if file is not None:
    df = pd.read_csv(file)
    st.write(df.head())
    st.subheader("Filter data")
    selected_column = st.selectbox("Column", df.columns)
    input = st.text_input("Value filter")
    filtered_df = df[df[selected_column] == input]
    st.write(filtered_df)

    st.subheader("Histogram")
    col1, col2 = st.columns(2)
    with col1:
        bins = st.slider("Number of bars", min_value=1, max_value=200)
    with col2:
        x_axis = st.selectbox("x axis", df.columns)
        fig, ax = plt.subplots()
        ax.hist(df[x_axis], bins)
        st.pyplot(fig)

    st.subheader("Chart")
    graph_type = st.selectbox("graph type", ["Plot", "Bar", "Scatter"])

    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("x axis", df.columns, key="x axis line")
    with col2:
        y_axis = st.selectbox("y axis", df.columns, key="y axis line")
    fig, ax = plt.subplots()

    if graph_type == "Plot":
        ax.plot(x_axis, y_axis, data=df)
    if graph_type == "Bar":
        ax.bar(x_axis, y_axis, data=df)
    if graph_type == "Scatter":
        ax.scatter(x_axis, y_axis, data=df)

    ax.set(xlabel=x_axis, ylabel=y_axis)

    st.pyplot(fig)

    st.subheader("Line chart")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("x axis", df.columns, key="x axis line chart")
    with col2:
        y_axis_list = st.multiselect(
            "y axis", df.columns, key="y axis line chart")
    st.line_chart(df, x=x_axis, y=y_axis_list)

    st.subheader("Area chart")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("x axis", df.columns, key="x axis area chart")
    with col2:
        y_axis = st.selectbox("y axis", df.columns, key="y axis area chart")
    st.area_chart(df, x=x_axis, y=y_axis)

    st.subheader("Bar chart")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("x axis", df.columns, key="x axis bar chart")
    with col2:
        y_axis_list = st.multiselect(
            "y axis", df.columns, key="y axis bar chart")
    st.bar_chart(df, x=x_axis, y=y_axis_list)

    st.subheader("Plotly")
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Vega lite")

    chart_data = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    st.vega_lite_chart(chart_data, {'mark': {'type': 'circle', 'tooltip': True},
                                    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
    })

    st.subheader("Pydeck chart")

    chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=chart_data,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

# Les widgets Streamlit exécutent automatiquement le script
# de haut en bas. Comme ce bouton n'est connecté à aucune
# autre logique, il ne fait que renvoyer un résultat vide.

# number = st.number_input("number input", min_value = 0, max_value = 10,step=2)
# text = st.text_area("input text multiple lines")
# date = st.date_input("date input")
st.button("Re-run")
