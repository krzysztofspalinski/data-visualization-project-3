import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.validators.scatter.marker import SymbolValidator
from data_generator_krzysztof import get_data
from random import randint
from plotly.validators.scatter.marker import SymbolValidator
import chart_studio.plotly as py
import plotly.figure_factory as ff
from heatmap_data_provider import getHeatmapData

def barplot_bad_graph():
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

def scatter_bad_graph(iris):
    
    fig = px.scatter(iris.rename(columns = {"species":"Gatunek",
                                            "sepal_length":"Długość kielicha",
                                            "sepal_width":"Szerokość kielicha",
                                            "petal_length":"Długość płatka",
                                            "petal_width":"Szerokość płatka"}),
                 x="Długość kielicha", y="Szerokość kielicha",
                 color = 'Długość płatka',size ='Szerokość płatka',
                 symbol = "Gatunek")
    
    fig.add_trace(go.Scatter(        
            x=iris['sepal_length'].loc[iris.species == 'nieznane'],
            y=iris['sepal_width'].loc[iris.species == 'nieznane'],
            showlegend=False,
            mode="markers+text",
            text = iris.loc[iris.species == 'nieznane'].id,
            marker=dict(color='black', size=0.0001)
        ), row = 1, col =1)

    fig.update_xaxes(
        title = "Długość kielicha", range=[0, 9]
    )
    fig.update_yaxes(
        title = "Szerokość kielicha", range=[0, 5]
    )
    fig.update_layout(title=dict(text="Irysy",
                                 x=0.5,
                                 y=0.95,
                                 font = dict(size=25),
                                 xanchor='center',        
                                 yanchor='top'),
                     legend=dict(orientation="h",
                            title="Gatunki"))
    
    return fig

def scatter_3d_bad_graph(seed=42):
	data_df = get_data(seed)

	companies = ['Firma 1', 'Firma 2', 'Firma 3', 'Firma 4']

	data = []

	gf = data_df.groupby('Company')

	for company in companies:
	    group = gf.get_group(company)
	    years = group['Year'].tolist()
	    length = len(years)
	    company_coords = [company] * length
	    product_A = group['Product A'].tolist()
	    product_B = group['Product B'].tolist()
	    
	    
	    data.append(dict(
	        type='scatter3d',
	        mode='lines',
	        x=years,
	        y=company_coords * 2 + [company_coords[0]],
	        z=product_A,
	        name='Produkt A, ' + company,
	        line=dict(
	            color='blue',
	            width=10
	        ),
	    ))
	    
	    data.append(dict(
	        type='scatter3d',
	        mode='lines',
	        x=years,
	        y=company_coords * 2 + [company_coords[0]],
	        z=product_B,
	        name='Produkt B, ' + company,
	        line=dict(
	            color='orange',
	            width=10
	        ),
	    ))
	    
	layout = dict(
	    title='Sprzedaż firm w latach 2010 - 2017',
	    showlegend=True,
	    scene=dict(
	        xaxis=dict(title=''),
	        yaxis=dict(title=''),
	        zaxis=dict(title=''),
	        camera=dict(
	            eye=dict(x=-1.7, y=-1.7, z=0.5)
	        )
	    )
	)
	fig_dict = dict(data=data, layout=layout)
	fig = go.Figure(fig_dict)   
	return fig

def piechart_bad_graph():

    def get_labels():
        return ['Golf', 'Mustang', 'Octavia', 'Multipla', 'Focus']

    def get_values(min, max):
        return [round(randint(min, max) / 10) * 10 for _ in range(5)]


    colors = ['#2afe38', '#22eb2f', '#1ad827', '#13c71e', '#0bb416']
    vals = get_values(100, 300)
    fig = go.Figure(data=[go.Pie(labels=get_labels(),
                                values=vals)])
    fig.update_traces(hoverinfo='skip', textinfo='label', textfont_size=16,
                    marker=dict(colors=colors))
    fig.update_layout(title_text=f'Liczba koni mechanicznych (suma {sum(vals)})')
    return fig

def heatmap_bad_graph(radius):    
    px.set_mapbox_access_token("") # INSERT TOKEN
    df = getHeatmapData()
    fig = px.density_mapbox(df, lat="Lat", lon="Lon", z="Population", radius=radius, color_continuous_scale=['red', 'red', 'yellow', 'green', 'cyan', 'blue', 'blue'])
    
    return fig