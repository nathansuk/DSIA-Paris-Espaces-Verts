from dash import Dash, html, dcc, callback, Output, Input
import data.GraphLib as gl
import layout.main_layout


graphlib = gl.GraphLib()  # Initialize GraphLib responsible for chart generation

graphlib.create_map()  # Save map in .html file in order to be displayed

app = Dash(__name__)

app.layout = layout.main_layout.create_main_layout(graphlib)


@app.callback(
    Output('id-graph2', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('selection-dropdown', 'value')]
)
def update_bar_chart(min_year, type_data):
    """
    Update the current openings / renovations per year plot
    :param min_year: Minimum year to visualize
    :param type_data: Type of data to visualize (1 for both, 2 for openings only, 3 for renovations only)
    :return: the new histogram figure
    """
    return graphlib.create_bar_chart_year_open(min_year, type_data)


if __name__ == '__main__':
    app.run(debug=True)
