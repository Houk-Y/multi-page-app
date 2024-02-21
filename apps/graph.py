# graph.py

import streamlit as st
import pandas as pd
from sklearn import datasets
import plotly.express as px


def app():
    st.title("Graph Page")

    st.write("This is the `Graph` page of the multi-page app.")

    st.write("The following is a graph of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    Y = pd.Series(iris.target, name="class")
    df = pd.concat([X, Y], axis=1)
    df["class"] = df["class"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

    # Create a scatter plot using Plotly
    fig = px.scatter(
        df,
        x="sepal length (cm)",
        y="sepal width (cm)",
        color="class",
        title="Sepal Length vs Sepal Width",
    )

    # Update layout
    fig.update_layout(xaxis_title="Sepal Length (cm)", yaxis_title="Sepal Width (cm)")

    # Show plot
    st.plotly_chart(fig)
