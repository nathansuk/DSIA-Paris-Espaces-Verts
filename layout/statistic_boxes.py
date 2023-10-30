from dash import Dash, html, dcc, callback, Output, Input


def create_statistics_boxes():
    layout = html.Div((

        html.Div((

            html.H3('Test'),
            html.H1('98')

        ), className='stat-box', id='box-red'),

        html.Div((

            html.H3('Test'),
            html.H1('98')

        ), className='stat-box', id='box-orange'),

        html.Div((

            html.H3('Test'),
            html.H1('98')

        ), className='stat-box', id='box-gp'),

        html.Div((

            html.H3('Test'),
            html.H1('98')

        ), className='stat-box', id='box-purple')


    ), id='stat-boxes')

    return layout