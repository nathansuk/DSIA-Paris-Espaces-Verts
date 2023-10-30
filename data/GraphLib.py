import pandas as pd
import plotly.express as px
from data.DataReader import DataReader
import folium
import json


class GraphLib:

    def __init__(self):
        self.data_reader = DataReader()

    # Return new pie chart showing space type repartition
    def create_pie_chart_space_type(self):
        fig = px.pie(self.data_reader.df, names="type_ev")
        return fig

    # Return new bar chart showing green spaces and their year when opened
    def create_bar_chart_year_open(self):
        data = self.data_reader.df.dropna(subset=['annee_ouverture'])
        data = data[data['annee_ouverture'] != 9999] # Deleting unusable data with year open equal to 9999
        count_by_year = data['annee_ouverture'].value_counts()
        test = pd.DataFrame({'année': count_by_year.index, 'count': count_by_year.values})
        fig = px.bar(test, x='année', y='count')
        return fig

    # Return a map with all green spaces polygons drawn
    def create_map(self):

        # Create new map centered on paris
        map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

        # Add polygons into the map
        for feature in self.data_reader.polygons['features']:
            if feature['geometry']:
                folium.GeoJson(feature['geometry']).add_to(map)

        map.save('carte.html')

    def create_bubble_charts_count(self):
        if 'adresse_codepostal' in self.data_reader.df.columns:
            # Count green spaces / zip code
            data = self.data_reader.df.groupby('adresse_codepostal').size().reset_index(name='Nombre d\'espaces verts')

            # Delete zip code > 76000 (arbitrary) to focus only on Paris
            data = data[data['adresse_codepostal'] <= 76000]
            fig = px.scatter(data, x='adresse_codepostal', y='Nombre d\'espaces verts', size='Nombre d\'espaces verts', color='Nombre d\'espaces verts', hover_name='adresse_codepostal')

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
            return fig

    def create_histogram_street_type(self):
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

        return fig

    def create_heatmap_surface(self):
        # Select total surface for hhorticulture and perimeter to see correlations
        correlations = self.data_reader.df[['surface_totale_reelle', 'surface_horticole', 'perimeter']]
        correlations = correlations.corr()

        # Créez la heatmap avec Plotly Express
        fig = px.imshow(correlations, x=correlations.index, y=correlations.columns,
                        labels=dict(color='Corrélation'), text_auto=True)
        fig.update_xaxes(side="top")
        return fig

