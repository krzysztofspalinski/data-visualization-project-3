import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os

def good_graph():
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop', title="Dobry wykres")
    return fig