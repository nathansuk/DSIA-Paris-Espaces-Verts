import pandas as pd
import os
import json


class DataReader:
    def __init__(self):
        # Get the path to /assets
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, '../assets/espaces_verts.csv')
        geojson_path = os.path.join(current_dir, '../assets/espaces_verts.geojson')

        self.df = pd.read_csv(csv_path, sep=';', encoding='utf8')

        # self.polygons will contain all geometry points to draw
        with open(geojson_path) as geojson_data:
            self.polygons = json.load(geojson_data)

    def get_df(self):
        return self.df
