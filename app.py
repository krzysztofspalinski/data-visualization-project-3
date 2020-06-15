# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import os
from joblib import load
import visdcc
import base64

from bad_graph_helper import barplot_bad_graph, scatter_bad_graph, scatter_3d_bad_graph
from good_graph_helper import barplot_good_graph, scatter_good_graph, scatter_3d_good_graph
from utils_iris import iris_data

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

analytics_image_filename = os.path.join(
    THIS_FOLDER, 'assets', 'Images', 'map_image.PNG')
analytics_image = base64.b64encode(open(analytics_image_filename, 'rb').read())
prediction_image_filename = os.path.join(
    THIS_FOLDER, 'assets', 'Images', 'prediction_image_v3.png')
prediction_image = base64.b64encode(
    open(prediction_image_filename, 'rb').read())

barplot_bad_graph = barplot_bad_graph()
barplot_good_graph = barplot_good_graph()
iris, correctAnwsers = iris_data()
scatter_bad_graph = scatter_bad_graph(iris)
scatter_good_graph = scatter_good_graph(iris)
scatter_3d_bad_graph = scatter_3d_bad_graph()
scatter_3d_good_graph = scatter_3d_good_graph()

app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    './styles.css',
])

server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            id='main',
            className='scroll-container',
            children=[
                html.Section(
                    id='title-section',
                    children=html.Div(
                        className='screen-height',
                        style={'align-items': 'center', 'display': 'flex',
                               'flex-direction': 'column', 'justify-content': 'center'},
                        children=[
                            html.H1("Jakaś strona tytułowa może?"),
                            html.H2("Albo bez..",
                                    style={'margin-bottom': '20px'}),
                            html.Div([
                                html.Div("9 ", style={'font-size': 60}),
                                html.Div("", style={'width': '10px'}),
                                html.Div("lat", style={'font-size': 25}),
                                html.Div("", style={'width': '50px'}),
                                html.Div("280 000 ", style={'font-size': 60}),
                                html.Div("", style={'width': '10px'}),
                                html.Div("firm", style={'font-size': 25}),
                                html.Div("", style={'width': '50px'}),
                                html.Div("5 ", style={'font-size': 60}),
                                html.Div("", style={'width': '10px'}),
                                html.Div("wydarzeń", style={'font-size': 25}),
                            ], style={'align-items': 'center', 'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center'}),
                            html.Div([
                                html.Div([
                                    html.H4(
                                        "Przekrój przestrzenny oraz gospodarczy działalności"),
                                    html.Div([
                                        html.Img(src='data:image/png;base64,{}'.format(analytics_image.decode()),
                                                 height=250)
                                    ]),
                                    html.Div("W jakim regionie firmy przetrwały najdłużej?", style={
                                             'font-size': 18}),
                                    html.Div("Które rodzaje działalności mają nawiększe szanse na sukces?", style={
                                             'font-size': 18}),
                                    html.Div("Kiedy najczęściej upadają firmy?", style={
                                             'font-size': 18}),
                                    dbc.Button(
                                        id='analysis-button',
                                        href='#1',
                                        children="Sprawdź",
                                        color='primary',
                                        style={'margin-top': '10px'}
                                    )
                                ], style={'align-items': 'center', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                                html.Div("", style={'width': '100px'}),
                                html.Div([
                                    html.H4("Predykcja życia firmy"),
                                    html.Div([
                                        html.Img(src='data:image/png;base64,{}'.format(prediction_image.decode()),
                                                 height=250)
                                    ]),
                                    html.Div("Jakie są Twoje szanse na sukces?", style={
                                             'font-size': 18}),
                                    html.Div("", style={'font-size': 18}),
                                    html.Div("", style={'font-size': 18}),
                                    dbc.Button(
                                        id='prediction-button',
                                        href='#2',
                                        children="Sprawdź",
                                        color='primary',
                                        style={'margin-top': '10px'}
                                    )
                                ], style={'align-items': 'center', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center', 'align-self': 'flex-start'}),
                            ], style={'align-items': 'center', 'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center',
                                      'padding-top': '50px'}),
                        ]
                    )
                ),
                html.Section(
                    id='barplot-section',
                    children=html.Div(
                        className='screen-height',
                        children=[html.Div(
                            style={'text-align': 'center'},
                            children=[
                                html.Div(
                                    children=[
                                        html.H1(
                                            children='Ilukrotnie wzrosło zadłużenie między okresem styczniowym a listopadowym?',
                                            style={'font-weight': 'bold',
                                                   'padding': '10px'}
                                        ),
                                        html.Div(
                                            children=[
                                                dcc.RadioItems(id='barplot-input',
                                                                options = [
                                                                    {'label': ' 2-krotnie', 'value': 'a'},
                                                                    {'label': ' O około 10%', 'value': 'b'},
                                                                    {'label': ' Nie da się określić', 'value': 'c'},
                                                                    ],
                                                                value = ""),
                                                html.P(id="barplot-wrong-answer", children="Źle!", style={'display': 'none'}),
                                                html.P(id="barplot-good-answer", children="Dobrze!", style={'display': 'none'})
                                            ]
                                        ),
                                        
                                        html.Button(
                                            'Sprawdź odpowiedź',
                                            id="barplot-check-answer-button",
                                        ),
                                        html.Div(id='barplot-number-of-clicks',
                                             style={'display': 'none'}, children='0')
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div([
                                                    dcc.Graph(figure=barplot_bad_graph),
                                                ], id='barplot-bad-graph', style={'display': 'inline-block'}),
                                                html.Div(id='barplot-good-graph', style={'display': 'inline-block'})]
                                        ), 
                                        html.Plaintext(id='barplot-explanation'),
                                    ], style={'display': 'inline-block'}
                                )
                            ]
                        )]
                    )
                ),
                html.Section(
                    id='scatter-section',
                    children=html.Div(
                        className='screen-height',
                        children=[html.Div(
                            style={'text-align': 'center'},
                            children=[
                                html.Div(
                                    children=[
                                        html.P('Mimo, że zazwyczaj dodawanie cech jest wygodną formą zwiększenia informacji, \
                                                ich nadmiar bywa zgubny. Poniższy wykres przedstawia znany w świecie uczenia maszynowego \
                                                zbiór irysów. Oś x przedstawia długość kielicha, oś y szerokość kielicha, kolor oznacza długość \
                                                płatka, natomiast wielkość punktów reprezentuje szerokość płatka. Poszczególne gatunki irysów \
                                                oznaczone  są różnymi symbolami.'),
                                        html.P(
                                            children='Twoim celem jest przypisanie punktów oznaczonych symbolem X \
                                                do odpowiedniego gatunku kwiatu (setosa, virginica, versicolor). \
                                                Porównaj wszystkie cztery cechy obiektów i sprawdź ile udało Ci się poprawnie odszyfrować!',
                                            style={'font-weight': 'bold'}
                                        ),
                                        html.Div(
                                            children=[
                                                html.P(children='Punkt 1 ',style={'display':'inline-block'} ),
                                                dcc.Dropdown(
                                                    id='scatter-input1',
                                                    options=[
                                                        {'label': 'setosa', 'value': 'setosa'},
                                                        {'label': 'virginica', 'value': 'virginica'},
                                                        {'label': 'versicolor', 'value': 'versicolor'}
                                                    ],
                                                    value='',
                                                    style={'width':'100px', 'display':'inline-block'}
                                                ),
                                                html.P(children=', punkt 2 ',style={'display':'inline-block'} ),
                                                dcc.Dropdown(
                                                    id='scatter-input2',
                                                    options=[
                                                        {'label': 'setosa', 'value': 'setosa'},
                                                        {'label': 'virginica', 'value': 'virginica'},
                                                        {'label': 'versicolor', 'value': 'versicolor'}
                                                    ],
                                                    value='',
                                                    style={'width':'100px', 'display':'inline-block'}
                                                ),
                                                html.P(children=', punkt 3 ',style={'display':'inline-block'} ),
                                                dcc.Dropdown(
                                                    id='scatter-input3',
                                                    options=[
                                                        {'label': 'setosa', 'value': 'setosa'},
                                                        {'label': 'virginica', 'value': 'virginica'},
                                                        {'label': 'versicolor', 'value': 'versicolor'}
                                                    ],
                                                    value='',
                                                    style={'width':'100px', 'display':'inline-block'}
                                                ),
                                                html.P(children=', punkt 4 ',style={'display':'inline-block'} ),
                                                dcc.Dropdown(
                                                    id='scatter-input4',
                                                    options=[
                                                        {'label': 'setosa', 'value': 'setosa'},
                                                        {'label': 'virginica', 'value': 'virginica'},
                                                        {'label': 'versicolor', 'value': 'versicolor'}
                                                    ],
                                                    value='',
                                                    style={'width':'100px', 'display':'inline-block'}
                                                ),
                                                html.P(children=', punkt 5',style={'display':'inline-block'} ),
                                                dcc.Dropdown(
                                                    id='scatter-input5',
                                                    options=[
                                                        {'label': 'setosa', 'value': 'setosa'},
                                                        {'label': 'virginica', 'value': 'virginica'},
                                                        {'label': 'versicolor', 'value': 'versicolor'}
                                                    ],
                                                    value='',
                                                    style={'width':'100px', 'display':'inline-block'}
                                                ),
                                                html.P(id="scatter-wrong-answer", children="Źle!", style={'display': 'none'}),
                                                html.P(id="scatter-good-answer", children="Dobrze!", style={'display': 'none'})
                                            ]
                                        ),
                                        
                                        html.Button(
                                            'Sprawdź odpowiedź',
                                            id="scatter-check-answer-button",
                                        ),
                                        html.Div(id='scatter-number-of-clicks',
                                             style={'display': 'none'}, children='0')
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div([
                                                    dcc.Graph(figure=scatter_bad_graph),
                                                ], id='scatter-bad-graph', style={'display': 'inline-block'}),
                                                html.Div(id='scatter-good-graph', style={'display': 'inline-block'})]
                                        ), 
                                        html.Plaintext(id='scatter-explanation'),
                                    ], style={'display': 'inline-block'}
                                )
                            ]
                        )]
                    )
                ),
                html.Section(
                    id='scatter-3d-section',
                    children=html.Div(
                        className='screen-height',
                        children=[html.Div(
                            style={'text-align': 'center'},
                            children=[
                                html.Div(
                                    children=[
                                        html.H1(
                                            children='Pytanie',
                                            style={'font-weight': 'bold',
                                                   'padding': '10px'}
                                        ),
                                        html.Div(
                                            children=[
                                                dcc.RadioItems(id='scatter-3d-input',
                                                                options = [
                                                                    {'label': ' Odp a', 'value': 'a'},
                                                                    {'label': ' Odp b', 'value': 'b'},
                                                                    {'label': ' Odp c', 'value': 'c'},
                                                                    ],
                                                                value = ""),
                                                html.P(id="scatter-3d-wrong-answer", children="Źle!", style={'display': 'none'}),
                                                html.P(id="scatter-3d-good-answer", children="Dobrze!", style={'display': 'none'})
                                            ]
                                        ),
                                        
                                        html.Button(
                                            'Sprawdź odpowiedź',
                                            id="scatter-3d-check-answer-button",
                                        ),
                                        html.Div(id='scatter-3d-number-of-clicks',
                                             style={'display': 'none'}, children='0')
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div([
                                                    dcc.Graph(figure=scatter_3d_bad_graph),
                                                ], id='scatter-3d-bad-graph', style={'display': 'inline-block'}),
                                                html.Div(id='scatter-3d-good-graph', style={'display': 'inline-block'})]
                                        ), 
                                        html.Plaintext(id='scatter-3d-explanation'),
                                    ], style={'display': 'inline-block'}
                                )
                            ]
                        )]
                    )
                ),
            ]),
        visdcc.Run_js(id='javascript',
                      run='''
                            new fullScroll({	
                                mainElement: 'main', 
                                sections:['title-section', 'barplot-section', 'scatter-section', 'scatter-3d-section'],
                                displayDots: true,
                                dotsPosition: 'right',
                                animateTime: 0.7,
                                animateFunction: 'ease'	
                            });
                            '''
                      ),
    ]
)

@app.callback([
    dash.dependencies.Output('barplot-good-graph', 'children'),
    dash.dependencies.Output('barplot-explanation', 'children'),
    dash.dependencies.Output('barplot-wrong-answer', 'style'),
    dash.dependencies.Output('barplot-good-answer', 'style'),
    dash.dependencies.Output('barplot-number-of-clicks', 'children')],
    [dash.dependencies.Input('barplot-check-answer-button', 'n_clicks'),
     dash.dependencies.Input('barplot-input', 'value'),],
    [dash.dependencies.State('barplot-number-of-clicks', 'children')])
def update_barplot_output(n_clicks, user_input, old_n_clicks):
    if n_clicks is not None and n_clicks > int(old_n_clicks):
        if user_input=="":
            return None, "Zaznacz odpowiedź!", {'display': 'none'}, {'display': 'none'}, str(n_clicks)
        else:
            explanation = "W styczniu 2017 Graf Kowalski wziął pożyczkę wysokości 80$. Odsetki wysokości 1% na miesiąc. \n \
                Oba wykresy przedstawiają stan zadłużenia Grafa, odnotowywany raz na 5 miesięcy począwszy od marca 2017 \n \
                (2 miesiące od zaciągnięcia pożyczki) do lipca 2020. \n \n \
                Autor lewego wykresu postanowił posortować oś X według nazw miesięcy, w których wypadały kolejne odnotowania stanu zadłużenia. \n \
                Wprowadza to czytelnika w błąd, sugerując, że przedstawione zdarzenia następowały chronologicznie. \n \
                Gubiąc faktyczną kolejność zdarzeń, a co za tym idzie rosnący charakter wykresu, użytkownik pomyśli, że Kowalski zaciąga kilkanaście \n \
                pożyczek na miesiąc i losowo niektóre spłaca. Po uważniejszym przyjrzeniu się odbiorca zauważy co najwyżej, że brakuje kilku miesięcy (np. maja) \n \
                i nie domyśli się co tak naprawdę wykres przedstawia. \n \n \
                Co więcej autor wykresu uzał, że skoro pożyczka wynosiła 80$, a najwyższa wartość zadłużenia to 122$, \n \
                dobrym pomysłem będzie przyjęcie tego przedziału za początek i koniec dla osi Y. \n \
                Powoduje to, że po pierwsze nie wiadomo ile tak naprawdę wynosiło zadłużenie odnotowane w lipcu, \n \
                a po drugie zaburza proporcje między słupkami. Na pierwszy rzut oka słupek 'Styczeń' \n \
                jest 2 razy mniejszy niż słupek 'Listopad', co sugeruje, że zadłużenie w listopadzie było dwukrotnie większe niż w styczniu. \n \
                Na prawym wykresie widzimy, że tak naprawdę wzrosło tylko ~1.11 razy."
            if user_input=="b":
                return dcc.Graph(figure=barplot_good_graph), explanation, {'display': 'none'}, {'color' : 'green', 'display': 'inline'}, str(n_clicks)
            else:
                return dcc.Graph(figure=barplot_good_graph), explanation, {'color' : 'red', 'display': 'inline'}, {'display': 'none'}, str(n_clicks)
    else:
        return None, "", {'display': 'none'}, {'display': 'none'}, old_n_clicks


@app.callback([
    dash.dependencies.Output('scatter-good-graph', 'children'),
    dash.dependencies.Output('scatter-explanation', 'children'),
    dash.dependencies.Output('scatter-wrong-answer', 'style'),
    dash.dependencies.Output('scatter-good-answer', 'style'),
    dash.dependencies.Output('scatter-number-of-clicks', 'children')],
    [dash.dependencies.Input('scatter-check-answer-button', 'n_clicks'),
     dash.dependencies.Input('scatter-input1', 'value'),
     dash.dependencies.Input('scatter-input2', 'value'),
     dash.dependencies.Input('scatter-input3', 'value'),
     dash.dependencies.Input('scatter-input4', 'value'),
     dash.dependencies.Input('scatter-input5', 'value')],
    [dash.dependencies.State('scatter-number-of-clicks', 'children')])
def update_scatter_output(n_clicks, input1, input2, input3, input4, input5, old_n_clicks):
    if n_clicks is not None and n_clicks > int(old_n_clicks):
        if input1=="" or input2=="" or input3=="" or input4=="" or input5=="":
            return None, "Zaznacz wszystkie odpowiedzi!", {'display': 'none'}, {'display': 'none'}, str(n_clicks)
        else:
            explanation = "I jak poszło? Czy zgodzisz się, że poprzedni wykres był chaotyczny? \n \
                Problemem poprzedniego wykresu jest jego wielowymiarowość, aż 4 zmienne (w dodatku ciągłe!) \n \
                są przedstawione graficznie, co powoduje, że każda z nich jest trudna do zinterpretowania. \n \
                Dla odmiany spójrz na poniższe dwa wykresy. W obecnej sytuacji wszystko jest dużo czytelniejsze. \n \
                Czy teraz uda Ci się poprawnie zidentyfikować te same obiekty? Dodatkowo korzystnie na czytelność \n \
                wykresu wpłynęło dostosowanie osi. W poprzednim wypadku około 60% wykersu było puste, obserwacje były \n \
                w jednym miejscu co jeszcze bardziej utrudniło interpretację. Teraz osie są przycięte, tak aby maksymalnie \n \
                wykorzystać potencjał wykresów. Są też odpowiednio podpisane, w związku z czym nie zgubisz żadnej informacji."
            if correctAnwsers[1]==input1 and \
                correctAnwsers[2]==input2 and \
                correctAnwsers[3]==input3 and \
                correctAnwsers[4]==input4 and \
                correctAnwsers[5]==input5:
                
                return dcc.Graph(figure=scatter_good_graph), explanation, {'display': 'none'}, {'color' : 'green', 'display': 'inline'}, str(n_clicks)
            else:
                return dcc.Graph(figure=scatter_good_graph), explanation, {'color' : 'red', 'display': 'inline'}, {'display': 'none'}, str(n_clicks)
    else:
        return None, "", {'display': 'none'}, {'display': 'none'}, old_n_clicks

@app.callback([
    dash.dependencies.Output('scatter-3d-good-graph', 'children'),
    dash.dependencies.Output('scatter-3d-explanation', 'children'),
    dash.dependencies.Output('scatter-3d-wrong-answer', 'style'),
    dash.dependencies.Output('scatter-3d-good-answer', 'style'),
    dash.dependencies.Output('scatter-3d-number-of-clicks', 'children')],
    [dash.dependencies.Input('scatter-3d-check-answer-button', 'n_clicks'),
     dash.dependencies.Input('scatter-3d-input', 'value'),],
    [dash.dependencies.State('scatter-3d-number-of-clicks', 'children')])
def update_scatter_3d_output(n_clicks, user_input, old_n_clicks):
    if n_clicks is not None and n_clicks > int(old_n_clicks):
        if user_input=="":
            return None, "Zaznacz odpowiedź!", {'display': 'none'}, {'display': 'none'}, str(n_clicks)
        else:
            explanation = "Wyjaśnienie"
            if user_input=="b":
                return dcc.Graph(figure=scatter_3d_good_graph), explanation, {'display': 'none'}, {'color' : 'green', 'display': 'inline'}, str(n_clicks)
            else:
                return dcc.Graph(figure=scatter_3d_good_graph), explanation, {'color' : 'red', 'display': 'inline'}, {'display': 'none'}, str(n_clicks)
    else:
        return None, "", {'display': 'none'}, {'display': 'none'}, old_n_clicks



if __name__ == '__main__':
    app.run_server(debug=True)
