import chart_studio.plotly as py
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from data_generator_krzysztof import get_data

def bad_graph(seed=42):
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