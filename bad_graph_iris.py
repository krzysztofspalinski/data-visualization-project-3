import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


def bad_graph(iris):
    
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