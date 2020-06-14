import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.validators.scatter.marker import SymbolValidator
import chart_studio.plotly as py
import plotly.figure_factory as ff
from heatmap_data_provider import getHeatmapData

def bad_graph():
    # colors = ['lightslategray',] * 9
    # colors[2] = 'crimson'
    fig = go.Figure(data=[go.Bar(
        x=['Styczeń', 'Luty', 'Marzec', 'Kwiecień',
            'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Listopad'],
        y=[90, 116, 82, 105, 95, 122, 90, 110, 100],
        # marker_color=colors,
        hoverinfo='skip'
    )])
    fig.update_layout(title_text='Stan zadłużenia w kolejnych okresach 5-miesięcznych', xaxis_title='Okres', yaxis_title='Zadłużenie')
    fig.update_yaxes(range=[80, 122], tickvals=[85, 95, 105, 115], showgrid=False, zeroline=False)
    return fig

def bad_heatgraph(radius):    
    px.set_mapbox_access_token("") # INSERT TOKEN
    df = getHeatmapData()
    fig = px.density_mapbox(df, lat="Lat", lon="Lon", z="Population", radius=radius, color_continuous_scale=['red', 'red', 'yellow', 'green', 'cyan', 'blue', 'blue'])
    
    return fig