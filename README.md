# Projet_PfDA_2020


## 🎆 Dossier Jupyter
Ce dossier contient le notebook utilisé pour nettoyer les données, entraîner les modèles et exporter le modèle retenu. 🐣
Le fichier du modèle retenu Model_RF.pkl et le fichier csv du dataset étaient trop lourd pour être mis sur Github.

## 🎯💻 Dossier apirest
Ce dossier contient l'API REST faite avec Django permettant de faire les prédictions avec le modèle qu'on a retenu dans le notebook. 
On peut également y mettre de nouveaux événements avec une requête POST et récupérer les événements qui y sont avec un GET.
Requêtes implémentées :
*  Get the events
```sh
❯ http://127.0.0.1:8000/events/
```
*  Get an event
```sh
❯ http://127.0.0.1:8000/event/{id}
```
*  Post an event : 
Testé via Postman
*  Predict remaining time of an event : 
Testé via Postman
