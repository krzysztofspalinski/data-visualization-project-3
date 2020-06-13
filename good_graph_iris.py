import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


def good_graph(iris):
    
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