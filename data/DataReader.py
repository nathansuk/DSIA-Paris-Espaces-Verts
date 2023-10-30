import pandas as pd
import os
import json
import requests


class DataReader:
    def __init__(self):
        # Get the path to /assets
        self.current_dir = os.path.dirname(__file__)
        self.polygons = self.set_geojson()  # self.polygons will contain all geometry points to draw
        self.df = self.generate_df_from_api()

    def set_geojson(self):
        geojson_path = os.path.join(self.current_dir, '../assets/espaces_verts.geojson')
        with open(geojson_path) as geojson_data:
            return json.load(geojson_data)

    def generate_df_from_api(self):
        api_endpoint = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/espaces_verts/exports/csv"
        response = requests.get(api_endpoint)
        with open('assets/datasets.csv', mode='wb') as file:
            file.write(response.content)
        csv_path = os.path.join(self.current_dir, '../assets/datasets.csv')
        return pd.read_csv(csv_path, sep=';', encoding='utf8')

    def get_df(self):
        return self.df
