import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
from plotly.subplots import make_subplots
from data_generator_krzysztof import get_data
from random import randint
from heatmap_data_provider import getHeatmapData
from pie_get_data import get_pie_data

def barplot_good_graph():
    x = 80
    x_sum = [x]
    for i in range(43):
        x += x*0.01
        x_sum.append(x)
    x_sum = np.round(np.array(x_sum))
    df = pd.DataFrame({'Wartość': x_sum[[2, 7, 12, 17, 22, 27, 32, 37, 42]],
                       'Miesiąc': ['Marzec', 'Sierpień', 'Styczeń',
                                   'Czerwiec', 'Listopad', 'Kwiecień',
                                   'Wrzesień', 'Luty', 'Lipiec']})

    fig = go.Figure(data=[go.Bar(name='Rok - 2017',
                                 x=['I - Marzec', 'II - Sierpień'],
                                 y=[82, 86],
                                 text=[82, 86],
                                 textposition='auto'
                                 ), go.Bar(name='Rok - 2018',
                                           x=['III - Styczeń',
                                               'IV - Czerwiec', 'V - Listopad'],
                                           y=[90, 95, 100],
                                           text=[90, 95, 100],
                                           textposition='auto'
                                           ), go.Bar(name='Rok - 2019',
                                                     x=['VI - Kwiecień',
                                                         'VII - Wrzesień'],
                                                     y=[105, 110],
                                                     text=[105, 110],
                                                     textposition='auto'
                                                     ), go.Bar(name='Rok - 2020',
                                                               x=['VIII - Luty',
                                                                   'IX - Lipiec'],
                                                               y=[116, 122],
                                                               text=[116, 122],
                                                               textposition='auto'
                                                               )])
    fig.update_xaxes(range=[-0.6, 8.6])
    fig.update_yaxes(tickprefix="$")
    fig.update_layout(title_text='Stan zadłużenia w kolejnych okresach 5-miesięcznych',
                      xaxis_title="Okres",
                      yaxis_title="Zadłużenie",
                      shapes=[
                          dict(
                              type="rect",
                              x0=-0.4,
                              y0=0,
                              x1=2,
                              y1=130,
                              opacity=0.5,
                              layer="below",
                              line_width=0,
                              fillcolor="LightSkyBlue",
                          ),
                          dict(
                              type="rect",
                              x0=2.0,
                              y0=0,
                              x1=4.4,
                              y1=130,
                              opacity=0.3,
                              layer="below",
                              line_width=0,
                              fillcolor="tomato",
                          ),
                          dict(
                              type="rect",
                              x0=4.4,
                              y0=0,
                              x1=6.8,
                              y1=130,
                              opacity=0.3,
                              layer="below",
                              line_width=0,
                              fillcolor="lawngreen",
                          ),
                          dict(
                              type="rect",
                              x0=6.8,
                              y0=0,
                              x1=9.2,
                              y1=130,
                              opacity=0.3,
                              layer="below",
                              line_width=0,
                              fillcolor="violet",
                          )
                      ])
    return fig

def scatter_good_graph(iris):
    fig = go.Figure()

    fig = make_subplots(1,2, subplot_titles=("Kielich", "Płatek"))

    for iris_type, color, shape in zip(['setosa', 'versicolor', 'virginica', 'nieznane'],
                                       ['#636EFA', '#EF553B', '#00CC96', 'black'],
                                      ['circle', 'diamond', 'square', 'x']):
        fig.add_trace(go.Scatter(        
            x=iris['sepal_length'].loc[iris.species == iris_type],
            y=iris['sepal_width'].loc[iris.species == iris_type],
            mode="markers",
            name=iris_type,
            marker=dict(color=color, size=5, symbol = shape)
        ), row = 1, col =1)


        fig.add_trace(go.Scatter(
            x=iris['petal_length'].loc[iris.species == iris_type],
            y=iris['petal_width'].loc[iris.species == iris_type],
            legendgroup="group",
            mode="markers",
            name=iris_type,
            marker=dict(color=color, symbol = shape),
            showlegend=False
        ), row = 1, col =2)

        if iris_type =="nieznane":
            fig.add_trace(go.Scatter(        
                x=iris['sepal_length'].loc[iris.species == iris_type],
                y=iris['sepal_width'].loc[iris.species == iris_type],
                mode="markers+text",
                text = iris.loc[iris.species == iris_type].id,
                textposition="bottom center",
                showlegend = False,
                marker=dict(color=color, size=5, symbol = shape)
            ), row = 1, col =1)

            fig.add_trace(go.Scatter(
                x=iris['petal_length'].loc[iris.species == iris_type],
                y=iris['petal_width'].loc[iris.species == iris_type],
                mode="markers+text",
                text = iris.loc[iris.species == iris_type].id,
                textposition="bottom center",
                marker=dict(color=color, symbol = shape),
                showlegend=False
            ), row = 1, col =2)

    fig.update_traces(marker=dict(size=6,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    fig.update_xaxes(
        title = "Długość"
    )
    fig.update_yaxes(
        title = "Szerokość"
    )
    fig.update_layout(title=dict(text="Irysy",
                                 x=0.5,
                                 y=0.9,
                                 font = dict(size=25),
                                 xanchor='center',        
                                 yanchor='top'))
    return fig

def scatter_3d_good_graph(seed=42):
	data_df = get_data(seed)

	gf = data_df.groupby('Company')
	fig = make_subplots(rows=2, cols=2,
	                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
	                           [{"secondary_y": True}, {"secondary_y": True}]],
	                   subplot_titles=('Firma 1', 'Firma 2', 'Firma 3', 'Firma 4'))


	company = 'Firma 1'
	group = gf.get_group(company)
	# Top left


	fig.add_trace(
	        go.Bar(
	            name='Produkt A',
	            x=list(group['Year']),
	            y=list(group['Product A']),
	            text=list(group['Product A'].round(1)),
	            textposition='auto',
	            offsetgroup=0,
	            marker_color='blue',
	            legendgroup='Produkt A'
	        ),
	    row=1, col=1, secondary_y=False,
	)

	fig.add_trace(
	        go.Bar(
	            name='Produkt B',
	            x=list(group['Year']),
	            y=list(group['Product B']),
	            text=list(group['Product B'].round(1)),
	            textposition='auto',
	            offsetgroup=1,
	            marker_color='orange',
	            legendgroup='Produkt B',
	        ),
	    row=1, col=1, secondary_y=False,
	)



	company = 'Firma 2'
	group = gf.get_group(company)

	# Top right

	fig.add_trace(
	        go.Bar(
	            name='Product A',
	            x=list(group['Year']),
	            y=list(group['Product A']),
	            text=list(group['Product A'].round(1)),
	            textposition='auto',
	            offsetgroup=0,
	            marker_color='blue',
	            legendgroup='Produkt A',
	            showlegend=False,
	        ),
	    row=1, col=2, secondary_y=False,
	)

	fig.add_trace(
	        go.Bar(
	            name='Product B',
	            x=list(group['Year']),
	            y=list(group['Product B']),
	            text=list(group['Product B'].round(1)),
	            textposition='auto',
	            offsetgroup=1, 
	            marker_color='orange',
	            legendgroup='Produkt B',
	            showlegend=False,
	        ),
	    row=1, col=2, secondary_y=False,
	)


	company = 'Firma 3'
	group = gf.get_group(company)
	# Bot left

	fig.add_trace(
	        go.Bar(
	            name='Product A',
	            x=list(group['Year']),
	            y=list(group['Product A']),
	            text=list(group['Product A'].round(1)),
	            textposition='auto',
	            offsetgroup=0,
	            marker_color='blue',
	            legendgroup='Produkt A',
	            showlegend=False,
	        ),
	    row=2, col=1, secondary_y=False,
	)

	fig.add_trace(
	        go.Bar(
	            name='Product B',
	            x=list(group['Year']),
	            y=list(group['Product B']),
	            text=list(group['Product B'].round(1)),
	            textposition='auto',
	            offsetgroup=1, 
	            marker_color='orange',
	            legendgroup='Produkt B',
	            showlegend=False,
	        ),
	    row=2, col=1, secondary_y=False,
	)


	company = 'Firma 4'
	group = gf.get_group(company)
	# Top left


	fig.add_trace(
	        go.Bar(
	            name='Product A',
	            x=list(group['Year']),
	            y=list(group['Product A']),
	            text=list(group['Product A'].round(1)),
	            textposition='auto',
	            offsetgroup=0, 
	            marker_color='blue',
	            legendgroup='Produkt A',
	            showlegend=False,
	        ),
	    row=2, col=2, secondary_y=False,
	)

	fig.add_trace(
	        go.Bar(
	            name='Product B',
	            x=list(group['Year']),
	            y=list(group['Product B']),
	            text=list(group['Product B'].round(1)),
	            textposition='auto',
	            offsetgroup=1, 
	            marker_color='orange',
	            legendgroup='Produkt B',
	            showlegend=False,
	        ),
	    row=2, col=2, secondary_y=False,
	)


	xaxes = ['xaxis', 'xaxis2', 'xaxis3', 'xaxis4']
	yaxes = [['yaxis', 'yaxis2'],['yaxis3', 'yaxis4'],['yaxis5', 'yaxis6'],['yaxis7', 'yaxis8']]

	for xaxis, yaxis in zip(xaxes, yaxes):
	    yaxis1 = yaxis[0]
	    yaxis2 = yaxis[1]
	    fig['layout'][xaxis]['title'] = 'Rok'
	    fig['layout'][xaxis]['showgrid'] = False
	    fig['layout'][xaxis]['dtick'] = 1
	    fig['layout'][yaxis1]['title'] = 'Sprzedaż produtku'
	    fig['layout'][yaxis1]['showgrid'] = True
	    fig['layout'][yaxis1]['range'] = [0, 85]
	    fig['layout'][yaxis2]['title'] = 'Łączna sprzedaż'
	    fig['layout'][yaxis2]['rangemode'] = 'tozero'
	    fig['layout'][yaxis2]['showgrid'] = False
	    fig['layout'][yaxis2]['range'] = [0, 150]
	fig.update_layout(legend=dict(x=0, y=-.15), legend_orientation="h", title='Sprzedaż firm w latach 2010 - 2017')
	return fig

def piechart_good_graph():
    brands = get_pie_data(2014)['brand']
    
    fig = go.Figure(data=[
        go.Bar(name='Rok 2014', x=brands, y=get_pie_data(2014)['price']),
        go.Bar(name='Rok 2015', x=brands, y=get_pie_data(2015)['price']),
        go.Bar(name='Rok 2016', x=brands, y=get_pie_data(2016)['price'])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group', yaxis_tickformat='d', title_text='Ceny poszczególnych marek samochodów w latach 2014-2016', yaxis_title='Cena w zł')
    return fig

def heatmap_good_graph(radius):
    px.set_mapbox_access_token("pk.eyJ1IjoicHJlc3RpIiwiYSI6ImNrYmR5c2dheTBnYnYyc3FlbzYwNG1oc3QifQ.UvQIxOoMc-UkTfNH4V5vFQ") # INSERT TOKEN
    df = getHeatmapData()
    fig = px.density_mapbox(df, lat="Lat", lon="Lon", z="Population", radius=radius, color_continuous_scale='rainbow')
    
    return fig