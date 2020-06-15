import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
from plotly.subplots import make_subplots


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