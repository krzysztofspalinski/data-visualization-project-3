import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
from plotly.subplots import make_subplots
from data_generator_krzysztof import get_data

def good_graph(seed=42):
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