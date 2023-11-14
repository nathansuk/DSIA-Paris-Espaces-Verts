
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

## Rapport d'analyse



Dans cette partie, il s'agira d'analyser succintement chaque graphiques généré.



### Répartition des types d'espace vert

Ce graphique en "camembert" montre les types d'espaces verts les plus présents dans Paris.

Type d'espace vert le plus présent : décorations sur la voie publique (33,2%)



### Nombre d'espaces verts ouverts et / ou rénovés par année

Ce graphique en barres montre les ouvertures et rénovations par année jusqu'en 2023.

Il s'agit d'un graphique dynamique et il est possible de modifier l'affichage pour voir uniquement les Ouvertures, Rénovations ou les deux.

Il est également possible de changer la date minimale d'affichage des données.



Le nombre d'ouvertures des espaces verts devient conséquent à partir des années 2000.

Un pic est observé en 2016 avec 107 ouvertures.



### Nombre d'espaces verts et surfaces cumulées par arrondissement

Le premier graphique en nuage de points montre le nombre d'espaces verts par arrondissement parisien.

L'arrondissement avec le plus d'espaces verts (tout type cumulé) est le 13ème (227 ev.), suivi du 19ème (217 ev.)



Il est intéressant de comparer la quantité avec les surfaces cumulées.



Le second graphique montre les surfaces totales réelles cumulées de tous les espaces verts par arrondissement.

On observe donc que le 12ème possède les espaces verts les plus conséquents (952 968 m²) suivis du 20 ème arrondissement (797 930m²)



### Répartition par type de voie

Ce graphique en barres (avec les axes x et y inverser) montre où se situent en majorité les espaces verts.

Ce graphique indique que les rues (1252) sont les types de voie où se situent le plus les espaces verts suivi des places (214).



### Histogramme du nombre d'espaces verts par intervalle de surface.

Cet histogramme montre le nombre d'espaces verts par tranche de surfaces (Respectivement : 0-100, 100-1000, 1000-10 000, 10 000-100 000,+100 000 m²)

Les espaces verts ont (en majorité) une surface comprise entre 100 et 1000 m²



### Géolocalisation des espaces verts parisiens

Cette carte est générée à l'aide du package "folium".

La création de la carte nécessite le fichier assets/espaces_verts.geojson qui permet de dessiner les polygones sur la carte.



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






