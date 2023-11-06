from dash import html


def create_statistics_boxes(statistics):
    """
    Get the statistics array from the DataReader to display them into 4 divs
    :param statistics: statistics array
    [number of rows, number of green areas opened in 2023, total surface, horticultural surface]
    :return: a html.Div containing all 4 divs
    """
    layout = html.Div((

        html.Div((

            html.H3("Nombre total d'espaces verts"),
            html.H1(statistics[0])

        ), className='stat-box', id='box-red'),

        html.Div((

            html.H3("Nouveaux espaces verts en 2023"),
            html.H1(statistics[3])

        ), className='stat-box', id='box-orange'),

        html.Div((

            html.H3("Surface totale des EV"),
            html.H1(f"{statistics[1]:,}".replace(".0", ' ') + " m²")

        ), className='stat-box', id='box-green'),

        html.Div((

            html.H3("Surface horticole totale"),
            html.H1(f"{statistics[2]:,}".replace(".0", ' ') + " m²")

        ), className='stat-box', id='box-purple'),


    ), id='stat-boxes')

    return layout
