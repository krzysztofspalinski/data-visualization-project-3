import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os


def good_graph():
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

    fig = go.Figure(data=[go.Bar(name='Pierwszy rok',
                                 x=['I - Marzec', 'II - Sierpień'],
                                 y=[82, 86],
                                 text=[82, 86],
                                 textposition='auto'
                                 ), go.Bar(name='Drugi rok',
                                           x=['III - Styczeń',
                                               'IV - Czerwiec', 'V - Listopad'],
                                           y=[90, 95, 100],
                                           text=[90, 95, 100],
                                           textposition='auto'
                                           ), go.Bar(name='Trzeci rok',
                                                     x=['VI - Kwiecień',
                                                         'VII - Wrzesień'],
                                                     y=[105, 110],
                                                     text=[105, 110],
                                                     textposition='auto'
                                                     ), go.Bar(name='Czwarty rok',
                                                               x=['VIII - Luty',
                                                                   'IX - Lipiec'],
                                                               y=[116, 122],
                                                               text=[116, 122],
                                                               textposition='auto'
                                                               )])
    fig.update_xaxes(range=[-0.6, 8.6])
    fig.update_yaxes(tickprefix="$")
    fig.update_layout(title_text='Skumulowane zadłużenie w kolejnych okresach 5-miesięcznych',
                      xaxis_title="Okres 5-miesięczny",
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
