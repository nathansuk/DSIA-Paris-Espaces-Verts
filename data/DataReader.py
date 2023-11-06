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
        """
        Load geojson file to get all green areas polygons
        Return : a json object containing polygons data
        """
        geojson_path = os.path.join(self.current_dir, '../assets/espaces_verts.geojson')
        with open(geojson_path) as geojson_data:
            return json.load(geojson_data)

    def generate_df_from_api(self):
        """
        Get the CSV file from Paris Open Data's API
        Write content as binary in assets/datasets.csv

        Return : the Dataframe from generated CSV
        """
        api_endpoint = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/espaces_verts/exports/csv"
        response = requests.get(api_endpoint)
        with open('assets/datasets.csv', mode='wb') as file:
            file.write(response.content)
        csv_path = os.path.join(self.current_dir, '../assets/datasets.csv')
        return pd.read_csv(csv_path, sep=';', encoding='utf8')

    def get_statistics(self):
        """
            Returns : an array with statistics in order
        """
        statistics = [self.df.shape[0],  # Row number
                      self.df['surface_totale_reelle'].sum(),  # Sum of real surfaces
                      self.df['surface_horticole'].sum(),  # Sum of horticultural surfaces
                      len(self.df[self.df["annee_ouverture"] == 2023])  # Count openings in 2023
                      ]

        return statistics

    def get_df(self):
        return self.df
