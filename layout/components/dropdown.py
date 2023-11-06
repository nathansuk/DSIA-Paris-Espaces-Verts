from dash import dcc


def create_selection_perso():
    """
    Create a new HTML dropdown to filter per type of data (openings / renovations / both)
    Return : the HTML dropdown
    """
    option = [{
        'label': 'Ouvertures et rénovations',
        'value': 1
    },
        {
            'label': 'Ouvertures uniquement',
            'value': 2
        },
        {
            'label': 'Rénovations uniquement',
            'value': 3
        }
    ]
    return dcc.Dropdown(
        id="selection-dropdown",
        options=option,
        value=1,
        clearable=False,
        style={'width': '50%'}
    )

def create_year_dropdown(df):
    """
    Create a new HTML dropdown to filter per years of openings
    Return : the dropdown HTML component
    """
    data = df.dropna(subset=['annee_ouverture'])
    annees_ouverture = sorted(data[data['annee_ouverture'] != 9999]['annee_ouverture'].dropna().unique())
    options = [{'label': str(int(annee)), 'value': annee} for annee in annees_ouverture]

    return dcc.Dropdown(
        id='year-dropdown',
        options=options,
        value=min(annees_ouverture),
        clearable=True,
        style={'width': '50%'}
    )
