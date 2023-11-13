
# Paris : espaces verts et assimilés

Ce projet, réalisé en Python, s'appuie sur des données disponibles sur l'Open Data de la Ville de Paris. L'objectif principal est d'explorer et d'analyser divers aspects des espaces verts et des assimilés parisiens, tels que leur répartition par type, leur surface, ainsi que les ouvertures / rénovations dans le temps.

Une présentation plus détaillées du jeu de données se trouve à l'adresse suivante : 
https://opendata.paris.fr/explore/dataset/espaces_verts/information/?disjunctive.type_ev&disjunctive.categorie&disjunctive.adresse_codepostal&disjunctive.presence_cloture

La récupération des données est dynamique, et se fait via l'API de Paris Open Data
## User Guide

Pour installer le projet commencez par 
cloner le dépôt : 

```
git clone https://github.com/nathansuk/DSIA-Paris-Espaces-verts 
```

Placez vous à la racine du répertoire et exécutez ensuite la commande :

```
python -m pip install -r requirements.txt
```

Les dépendances nécessaires vont s'installer.

Pour démarrer le dashboard : (toujours à la racine)
```
python main.py
```

Et rendez-vous sur : http://127.0.0.1/8050

## Developer Guide

Architecture :
![alt text](https://i.ibb.co/xz8TB57/Capture-d-cran-2023-11-13-123755.png)
 
## Package data

| Objet             | Responsabilité                                                                |
| ----------------- | ------------------------------------------------------------------ |
| DataReader | Récupère les données de l'API et les stocke dans assets/datasets.csv |
| GraphLib | Chaque méthode retourne un des graphiques à destination du dashboard  |

## Package layout

| Fichiers            | Responsabilité                                                                |
| ----------------- | ------------------------------------------------------------------ |
| /layout/*.py | Structure la page HTML dans sa globalité |
| /layout/components | Retourne des petits composants HTML  |

## Autres dossiers

| Dossier            | Responsabilité                                                                |
| ----------------- | ------------------------------------------------------------------ |
| /tests/ | Contient des fichiers python des tests de chaque graphique et de l'API  |
| /assets/ | Contient les jeux de données .csv et .geojson et le fichier style.css  |

### Notes supplémentaires: 
Le fichier .geojson est un fichier à part pour géolocaliser les données des espaces verts, provient du même site que le jeu de données original.






