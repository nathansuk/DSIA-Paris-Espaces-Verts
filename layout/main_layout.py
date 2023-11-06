from dash import dcc, html
import layout.statistic_boxes
import layout.components.dropdown
import layout.components.map


def create_main_layout(graphlib):
    """
    Create the main layout
    :param graphlib: the graphlib object used to generate plots
    :return: the main layout
    """
    main_layout = html.Div([
        html.H1(children='Paris : Espaces verts et assimilés'),
        layout.statistic_boxes.create_statistics_boxes(graphlib.data_reader.get_statistics()),

        html.Div([

            dcc.Graph(id='id-graph', figure=graphlib.create_pie_chart_space_type(), className='flex-item graph1'),

            html.Div([
                dcc.Graph(id='id-graph2', figure=graphlib.create_bar_chart_year_open(), className='flex-item graph2'),
                html.Div([
                    html.H3("Voir les données à partir de l'année: "),
                    layout.components.dropdown.create_year_dropdown(graphlib.data_reader.df),
                    html.H3('Afficher les : '),
                    layout.components.dropdown.create_selection_perso()
                ], className='perso-selection')
            ], className='flex-item graph2-container'),

        ], className='flex-container'),

        html.Div([
            dcc.Graph(id='id-graph3', figure=graphlib.create_bubble_charts_count(), className='flex-item graph3'),
            dcc.Graph(id='id-graph6', figure=graphlib.create_scatter_surfaces(), className='flex-item graph6'),
            dcc.Graph(id='id-graph4', figure=graphlib.create_histogram_street_type(), className='flex-item graph4'),
        ], className='flex-container'),

        html.Div([

            dcc.Graph(id='id-graph5', figure=graphlib.create_heatmap_surface(), className='flex-item graph5'),

            html.H1("Représentation des espaces verts parisiens"),
            layout.components.map.create_iframe_map()
        ], className='flex-container')

    ], id='main-container')

    return main_layout