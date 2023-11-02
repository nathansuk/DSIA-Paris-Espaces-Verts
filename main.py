from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import data.GraphLib as gl
import layout.statistic_boxes


graphlib = gl.GraphLib()

graphlib.create_map()  # Save map in .html file in order to be displayed

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Paris : Espaces verts et assimilés'),
    layout.statistic_boxes.create_statistics_boxes(),

    html.Div([

        dcc.Graph(id='id-graph', figure=graphlib.create_pie_chart_space_type(), className='flex-item graph1'),

        html.Div([
            dcc.Graph(id='id-graph2', figure=graphlib.create_bar_chart_year_open(), className='flex-item graph2'),
            html.Div([
                html.H3("Voir les données à partir de l'année: "),
                graphlib.create_year_dropdown(),
                html.H3('Afficher les : '),
                graphlib.create_selection_perso()
            ], className='perso-selection')
        ], className='flex-item graph2-container'),

    ], className='flex-container'),

    html.Div([
        dcc.Graph(id='id-graph3', figure=graphlib.create_bubble_charts_count(), className='flex-item graph3'),
        dcc.Graph(id='id-graph4', figure=graphlib.create_histogram_street_type(), className='flex-item graph4'),
    ], className='flex-container'),

    html.Div([
        dcc.Graph(id='id-graph5', figure=graphlib.create_heatmap_surface(), className='flex-item graph5'),

        html.H1("Représentation des espaces verts parisiens"),
        html.Iframe(id='map', srcDoc=open('carte.html', 'r').read(), width='100%', height='500', className='flex-item graph5')
    ], className='flex-container')

], id='main-container')


@app.callback(
    Output('id-graph2', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('selection-dropdown', 'value')]
)
def update_bar_chart(min_year, type_data):
    return graphlib.create_bar_chart_year_open(min_year, type_data)


if __name__ == '__main__':
    app.run(debug=True)
