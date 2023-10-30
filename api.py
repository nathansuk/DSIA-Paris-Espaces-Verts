import requests

def download_dataset():
    api_endpoint = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/espaces_verts/exports/csv"
    response = requests.get(api_endpoint)

    with open('assets/datasets.csv', mode='wb') as file:
        file.write(response.content)

    print(response.status_code)


download_dataset()