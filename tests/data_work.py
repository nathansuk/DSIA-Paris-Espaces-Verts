import json

import pandas as pd
import plotly.express as px
import folium
import geopandas as gpd

df = pd.read_csv('../assets/espaces_verts.csv', sep=';', encoding='utf8')


def creer_piechart_type_espace():
    df = pd.read_csv('../assets/espaces_verts.csv', sep=';', encoding='utf8')
    piechart = px.pie(df, names="Typologie d'espace vert")
    return piechart


def creer_histo():
    df = pd.read_csv('../assets/espaces_verts.csv', sep=';', encoding='utf8')
    df = df.dropna(subset=['Année de l\'ouverture'])
    df = df[df['Année de l\'ouverture'] != 9999]
    count_by_year = df['Année de l\'ouverture'].value_counts()
    test = pd.DataFrame({ 'année': count_by_year.index, 'count': count_by_year.values})
    print(test)

    fig = px.bar(test, x='année', y='count')

    fig.show()


def creer_map_folium():
    # Charger le fichier .geojson
    with open('../assets/espaces_verts.geojson') as f:
        data = json.load(f)

    # Créer une carte centrée sur une certaine latitude et longitude
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    # Ajouter les polygones à la carte
    for feature in data['features']:
        if feature['geometry']:
            folium.GeoJson(feature['geometry']).add_to(m)

    m.save('carte.html')


def creer_bubble_charts():
    if 'Code postal' in df.columns:
        # Groupement par code postal + le nombre d'espaces verts dans chaque code postal
        data = df.groupby('Code postal').size().reset_index(name='Nombre d\'espaces verts')

        # Suppression des valeurs "aberrantes" avec un code postal > à celui de paris, puisque 1 espace verts seulement
        data = data[data['Code postal'] <= 76000]

        fig = px.scatter(data, x='Code postal', y='Nombre d\'espaces verts', size='Nombre d\'espaces verts',
                         color='Nombre d\'espaces verts', hover_name='Code postal')

        # Mettez à jour les étiquettes des axes
        fig.update_xaxes(title_text='Code postal')
        fig.update_xaxes(
            tickvals=[75001, 75002, 75003, 75004, 75005, 75006, 75007, 75008, 75009, 75010, 75011, 75012, 75013, 75014,
                      75015, 75016, 75017, 75018, 75019, 75020],
            ticktext=['75001', '75002', '75003', '75004', '75005', '75006', '75007', '75008', '75009', '75010', '75011',
                      '75012', '75013', '75014', '75015', '75016', '75017', '75018', '75019', '75020'])
        fig.update_yaxes(title_text='Nombre d\'espaces verts')

        fig.show()

def create_histogram_street_type():
    df = pd.read_csv('../assets/espaces_verts.csv', sep=';', encoding='utf8')
    df['Adresse - type voie'] = df['Adresse - type voie'].str.split().str[0]
    df = df[df['Adresse - type voie'] != 'ND']
    df['Adresse - type voie'] = df['Adresse - type voie'].str.replace('rue', 'RUE')
    # Compter le nombre d'occurrences de chaque type de voie
    typevoie_counts = df['Adresse - type voie'].value_counts().reset_index()
    # Renommer les colonnes
    typevoie_counts.columns = ['Adresse - type voie', 'Count']
    typevoie_counts = typevoie_counts.sort_values(by='Count', ascending=True)


    # Créer le graphique en anneau
    fig = px.bar(typevoie_counts, x='Count', y='Adresse - type voie',
                 title='Répartition des Types de Voies',
                 labels={'Adresse - type voie': 'Type de Voie', 'Count': 'Nombre d\'Espaces Verts'},)

    # Afficher le graphique
    return fig

def create_heatmap_surface():
    # Sélectionnez les variables pertinentes pour la heatmap
    correlations = df[['Superficie totale réelle', 'Surface horticole', 'Périmètre']]

    # Calculez la matrice de corrélation
    correlations = correlations.corr()

    # Créez la heatmap avec Plotly Express
    fig = px.imshow(correlations, x=correlations.index, y=correlations.columns,
                    labels=dict(color='Corrélation'), text_auto=True)
    fig.update_xaxes(side="top")
    fig.show()