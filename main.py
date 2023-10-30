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

    html.Div((

        dcc.Graph(id='id-graph', figure=graphlib.create_pie_chart_space_type(),
                  style={'backgroundColor': 'red', 'border-radius': '15px'}),
        dcc.Graph(id='id-graph2', figure=graphlib.create_bar_chart_year_open()),
        dcc.Graph(id='id-graph3', figure=graphlib.create_bubble_charts_count()),
        dcc.Graph(id='id-graph4', figure=graphlib.create_histogram_street_type()),
        dcc.Graph(id='id-graph5', figure=graphlib.create_heatmap_surface()),
        # Source : https://medium.com/@shachiakyaagba_41915/integrating-folium-with-dash-5338604e7c56
        html.Iframe(id='map', srcDoc=open('carte.html', 'r').read(), width='90%', height='500')

    ), id='graphs-container')

], id='main-container')

"""
@callback(
    Output('id-graph', 'figure')
)
"""

if __name__ == '__main__':
    app.run(debug=True)
