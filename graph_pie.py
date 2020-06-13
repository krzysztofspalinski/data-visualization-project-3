import plotly.express as px
import plotly.graph_objects as go
from random import randint

def get_labels():
    return ['Golf', 'Mustang', 'Octavia', 'Multipla', 'Focus']

def get_values(min, max):
    return [round(randint(min, max) / 10) * 10 for _ in range(5)]

def bad_graph():
    colors = ['#2afe38', '#22eb2f', '#1ad827', '#13c71e', '#0bb416']
    vals = get_values(100, 300)
    fig = go.Figure(data=[go.Pie(labels=get_labels(),
                                values=vals)])
    fig.update_traces(hoverinfo='skip', textinfo='label', textfont_size=16,
                    marker=dict(colors=colors))
    fig.update_layout(title_text=f'Liczba koni mechanicznych (suma {sum(vals)})')
    fig.show()
    return fig

def good_graph():
    vals_labels = [x for x in sorted(zip(get_values(100, 300), get_labels()))]
    labels = [x[1] for x in vals_labels]
    vals = [x[0] for x in vals_labels]

    fig = go.Figure(go.Bar(
                x=vals,
                y=labels,
                orientation='h',
                marker=dict(
                    color='green'
                ),
                hoverinfo='skip'))
    fig.update_layout(
        xaxis=dict(
            range=[0,300],
            dtick=10
        )
    )
    fig.show()
    return fig