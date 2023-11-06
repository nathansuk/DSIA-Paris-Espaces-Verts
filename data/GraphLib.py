import pandas as pd
import plotly.express as px
from data.DataReader import DataReader
import folium
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import dcc


class GraphLib:

    def __init__(self):
        self.data_reader = DataReader()

    def create_pie_chart_space_type(self):
        """
        Create a new pie chart figure representing green areas type repartition
        Return : the pie chart figure
        """
        fig = px.pie(self.data_reader.df, names="type_ev")
        fig.update_layout(
            title="Répartition des Types d'espaces verts",
            font=dict(
                family="Wix Madefor Text",
                size=13
            )
        )
        return fig

    def create_bar_chart_year_open(self, min_year=None, type_data=1):
        """
        Create a new histogram figure representing when green areas has been opened (or renovated) per year
        Params:
            min_year : In case we want a representation after a specific date. Default  = None (no date minimum)
            type_data : 1 for all type of data (openings / renavations), 2 for openings only, 3 for renovations only
        Return : the histogram figure(treated)
        """

        data = self.data_reader.df.dropna(subset=['annee_ouverture'])
        data_renovation = self.data_reader.df.dropna(subset=['annee_renovation'])

        data = data[data['annee_ouverture'] != 9999]  # Delete unusable data > 9999 (corresponding to NA)

        if min_year is not None:  # If minimum date has been defined
            data = data[data['annee_ouverture'] >= min_year]

        count_by_year = data['annee_ouverture'].value_counts()
        count_renovations = data_renovation['annee_renovation'].value_counts()

        openings = pd.DataFrame({'Année': count_by_year.index, "Nombre d'ouvertures": count_by_year.values, 'Type': 'Ouvertures'})
        renovations = pd.DataFrame({'Année': count_renovations.index, "Nombre de rénovations": count_renovations.values, 'Type': 'Rénovations'})

        if type_data == 1:
            combined_df = pd.concat([openings, renovations], ignore_index=True)  # Concat openings and renovations dataframes
        elif type_data == 2:
            combined_df = openings  # Keep only openings dataframe
        elif type_data == 3:
            combined_df = renovations  # Keep only renovations dataframe

        fig = make_subplots(specs=[[{"secondary_y": False}]])

        if 'Nombre d\'ouvertures' in combined_df.columns:
            fig.add_trace(
                go.Bar(x=combined_df['Année'], y=combined_df['Nombre d\'ouvertures'], name="Nombre d'ouvertures"),
                secondary_y=False,
            )

        if 'Nombre de rénovations' in combined_df.columns:
            fig.add_trace(
                go.Bar(x=combined_df['Année'], y=combined_df['Nombre de rénovations'], name="Nombre de rénovations"),
                secondary_y=False,
            )
            if 'Nombre d\'ouvertures' not in combined_df.columns:
                fig.update_traces(marker=dict(color='red'))

        fig.update_layout(
            title="Nombre d'espaces verts ouverts et rénovés par année",
            xaxis_title="Année",
            yaxis_title="Nombre d'ouvertures / rénovations",
            yaxis2=dict(title="Nombre de rénovations", overlaying='y', side='right'),
            font=dict(family="Wix Madefor Text", size=13)
        )

        return fig

    def create_year_dropdown(self):
        """
        Create a new HTML dropdown to filter per years of openings
        Return : the dropdown HTML component
        """
        data = self.data_reader.df.dropna(subset=['annee_ouverture'])
        annees_ouverture = sorted(data[data['annee_ouverture'] != 9999]['annee_ouverture'].dropna().unique())
        options = [{'label': str(int(annee)), 'value': annee} for annee in annees_ouverture]

        return dcc.Dropdown(
            id='year-dropdown',
            options=options,
            value=min(annees_ouverture),
            clearable=True,
            style={'width': '50%'}
        )


    # Return a map with all green spaces polygons drawn
    def create_map(self):
        """
        Save a new .html file with a map filled with polygons
        Polygons are generated with the assets/.geojson file
        """
        # Create new map centered on paris
        map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)  # New map centered on Paris

        # Draw polygons into the map
        for feature in self.data_reader.polygons['features']:
            if feature['geometry']:
                folium.GeoJson(feature['geometry']).add_to(map)

        map.save('carte.html')

    def create_bubble_charts_count(self):
        """
        Create a new bubble chart figure counting total of green areas / district.
        Return : the bubble chart figure
        """
        if 'adresse_codepostal' in self.data_reader.df.columns:
            # Count green areas / zip code
            data = self.data_reader.df.groupby('adresse_codepostal').size().reset_index(name='Nombre d\'espaces verts')

            # Delete zip code > 76000 (arbitrary) to focus only on Paris
            data = data[data['adresse_codepostal'] <= 76000]
            fig = px.scatter(data, x='adresse_codepostal',
                                   y='Nombre d\'espaces verts',
                                   size='Nombre d\'espaces verts',
                                   color='Nombre d\'espaces verts',
                                   hover_name='adresse_codepostal',
                                   title="Nombre d'espaces verts par arrondissement")

            # Update x,y axes
            fig.update_xaxes(title_text='Code postal')
            fig.update_xaxes(
                tickvals=[75001, 75002, 75003, 75004, 75005, 75006, 75007, 75008, 75009, 75010, 75011, 75012, 75013,
                          75014,
                          75015, 75016, 75017, 75018, 75019, 75020],
                ticktext=['75001', '75002', '75003', '75004', '75005', '75006', '75007', '75008', '75009', '75010',
                          '75011',
                          '75012', '75013', '75014', '75015', '75016', '75017', '75018', '75019', '75020'])
            fig.update_yaxes(title_text='Nombre d\'espaces verts')
            fig.update_layout(
                font=dict(
                    family="Wix Madefor Text",
                    size=13
                )
            )
            return fig

    def create_scatter_surfaces(self):
        """
            Create a new scatter plot counting total of green areas surface / district.
            Return : the scatter plot
        """
        surface_par_arrondissement = self.data_reader.df.groupby('adresse_codepostal')['surface_totale_reelle'].sum().reset_index()
        surface_par_arrondissement = surface_par_arrondissement[
            surface_par_arrondissement['adresse_codepostal'] <= 76000]

        fig = px.scatter(surface_par_arrondissement,
                         x='adresse_codepostal',
                         y='surface_totale_reelle',
                         labels={'adresse_codepostal': 'Code Postal',
                                 'surface_totale_reelle': 'Surfaces totales réelles cumulées'},
                         title='Surfaces cumulées des espaces verts par arrondissement',
                         size='surface_totale_reelle',
                         color='surface_totale_reelle')

        fig.update_xaxes(
            tickvals=[75001, 75002, 75003, 75004, 75005, 75006, 75007, 75008, 75009, 75010, 75011, 75012, 75013,
                      75014,
                      75015, 75016, 75017, 75018, 75019, 75020],
            ticktext=['75001', '75002', '75003', '75004', '75005', '75006', '75007', '75008', '75009', '75010',
                      '75011',
                      '75012', '75013', '75014', '75015', '75016', '75017', '75018', '75019', '75020'])

        return fig

    def create_histogram_street_type(self):
        """
        Create a new histogram plot showing green areas repartition per type of street
        Return : the histogram plot
        """
        df = self.data_reader.df

        # Keep only first word from 'Adresse type voie' ex : "RUE" because "RUE DE" and "RUE LA" were different
        df['adresse_typevoie'] = df['adresse_typevoie'].str.split().str[0]

        # Delete the only "NON DEFINED"
        df = df[df['adresse_typevoie'] != 'ND']

        # Replace the only line with 'rue' by 'RUE'
        df['adresse_typevoie'] = df['adresse_typevoie'].str.replace('rue', 'RUE')

        # Count occurrences for every type of street
        street_type_counts = df['adresse_typevoie'].value_counts().reset_index()

        street_type_counts.columns = ['adresse_typevoie', 'Count']

        # Sort descending
        street_type_counts = street_type_counts.sort_values(by='Count', ascending=True)

        fig = px.bar(street_type_counts, x='Count', y='adresse_typevoie',
                     title='Répartition des Types de Voies',
                     labels={'adresse_typevoie': 'Type de Voie', 'Count': 'Nombre d\'Espaces Verts'}, )
        fig.update_layout(
            font=dict(
                family="Wix Madefor Text",
                size=13
            )
        )
        return fig

    def create_heatmap_surface(self):
        """
        Create a new correlation matrix showing relation between type of surfaces
        Return : correlation matrix figure
        """
        # Select total surface for hhorticulture and perimeter to see correlations
        correlations = self.data_reader.df[['surface_totale_reelle', 'surface_horticole', 'perimeter']]
        correlations = correlations.corr()

        fig = px.imshow(correlations, x=correlations.index, y=correlations.columns,
                        labels=dict(color='Corrélation'), text_auto=True)
        fig.update_xaxes(side="top")
        fig.update_layout(
            font=dict(
                family="Wix Madefor Text",
                size=13
            )
        )
        return fig

